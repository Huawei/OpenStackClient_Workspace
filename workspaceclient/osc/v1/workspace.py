#   Copyright 2016 Huawei, Inc. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
import logging

from osc_lib.command import command
from workspaceclient.common.i18n import _
from workspaceclient.osc.v1 import parser_builder as pb
from workspaceclient.v1 import resource

LOG = logging.getLogger(__name__)


class EnableWorkspace(command.Command):
    _description = _("create workspace")

    def get_parser(self, prog_name):
        parser = super(EnableWorkspace, self).get_parser(prog_name)
        pb.Workspace.add_domain_type_option(parser)
        pb.Workspace.add_domain_name_option(parser)
        pb.Workspace.add_domain_admin_account_option(parser)
        pb.Workspace.add_domain_password_option(parser)
        pb.Workspace.add_active_domain_ip_option(parser)
        pb.Workspace.add_active_dns_ip_option(parser)
        pb.Workspace.add_standby_domain_ip_option(parser)
        pb.Workspace.add_standby_dns_ip_option(parser)
        pb.Workspace.add_vpc_option(parser)
        pb.Workspace.add_subnets_option(parser)
        pb.Workspace.add_access_mode_option(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        network = self.app.client_manager.network

        vpc_id = network.find_network(args.vpc).id
        subnet_ids = [network.find_subnet(subnet).id
                      for subnet in args.subnets]
        job = client.workspaces.enable(
            args.domain_type, args.domain_name, args.domain_admin_account,
            args.domain_password, vpc_id, subnet_ids, args.access_mode,
            active_domain_ip=args.active_domain_ip,
            active_dns_ip=args.active_dns_ip,
            standby_domain_ip=args.standby_domain_ip,
            standby_dns_ip=args.standby_dns_ip,
        )
        return "Request Received, job id: %s" % job["job_id"]


class ShowWorkspace(command.ShowOne):
    _description = _("show workspace")

    def get_parser(self, prog_name):
        parser = super(ShowWorkspace, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        workspace = client.workspaces.get()
        columns = resource.Workspace.show_column_names
        formatter = resource.Workspace.formatter
        outputs = workspace.get_display_data(columns, formatter=formatter)
        return columns, outputs


class EditWorkspace(command.Command):
    _description = _("show workspace")

    def get_parser(self, prog_name):
        parser = super(ShowWorkspace, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        products = client.workspaces.edit()
        columns = resource.Product.list_column_names
        outputs = [r.get_display_data(columns) for r in products]
        return columns, outputs


class DisableWorkspace(command.Command):
    _description = _("disable workspace")

    def get_parser(self, prog_name):
        parser = super(DisableWorkspace, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        job = client.workspaces.disable()
        return "Request Received, job id: %s" % job["job_id"]
