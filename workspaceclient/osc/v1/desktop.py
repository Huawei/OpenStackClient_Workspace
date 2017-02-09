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

from osc_lib import utils
from osc_lib.command import command
from workspaceclient.common import parser_builder as p
from workspaceclient.common.i18n import _
from workspaceclient.osc.v1 import parser_builder as pb
from workspaceclient.v1 import resource

LOG = logging.getLogger(__name__)


class ListDesktop(command.Lister):
    _description = _("list desktops")

    def get_parser(self, prog_name):
        parser = super(ListDesktop, self).get_parser(prog_name)
        pb.DesktopParser.add_status_option(parser)
        pb.DesktopParser.add_desktop_ip_option(parser)
        pb.DesktopParser.add_user_name_option(parser)
        pb.DesktopParser.add_computer_name_option(parser)
        pb.DesktopParser.add_marker_option(parser)
        p.BaseParser.add_limit_option(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        desktops = client.desktop.list(args.desktop_ip, args.status,
                                       args.user_name, args.computer_name,
                                       args.marker, args.limit)
        columns = resource.Desktop.list_column_names
        data = [r.get_display_data(columns) for r in desktops]
        return columns, data


class ListDesktopDetail(command.Lister):
    _description = _("list desktops with detail")

    def get_parser(self, prog_name):
        parser = super(ListDesktopDetail, self).get_parser(prog_name)
        pb.DesktopParser.add_status_option(parser)
        pb.DesktopParser.add_desktop_ip_option(parser)
        pb.DesktopParser.add_user_name_option(parser)
        pb.DesktopParser.add_computer_name_option(parser)
        pb.DesktopParser.add_marker_option(parser)
        p.BaseParser.add_limit_option(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        desktops = client.desktop.list_detail(args.desktop_ip,
                                              args.status,
                                              args.user_name,
                                              args.computer_name,
                                              args.marker,
                                              args.limit)
        columns = resource.Desktop.list_detail_column_names
        data = [r.get_display_data(columns) for r in desktops]
        return columns, data


class RebootDesktop(command.Command):
    _description = _("reboot desktop")

    def get_parser(self, prog_name):
        parser = super(RebootDesktop, self).get_parser(prog_name)
        pb.DesktopParser.add_desktop_id_arg(parser, 'reboot')
        pb.DesktopParser.add_hard_or_soft_arg(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        desktop = client.desktop.find(args.desktop_id)
        client.desktop.reboot(desktop.desktop_id, args.force)
        return "done"


class CreateDesktop(command.Command):
    _description = _("Create a new desktop")

    def get_parser(self, prog_name):
        parser = super(CreateDesktop, self).get_parser(prog_name)
        pb.DesktopParser.add_desktop_id_arg(parser, 'create')
        pb.DesktopParser.add_hard_or_soft_arg(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        return args


class StartDesktop(command.Command):
    _description = _("Start desktop")

    def get_parser(self, prog_name):
        parser = super(StartDesktop, self).get_parser(prog_name)
        pb.DesktopParser.add_desktop_id_arg(parser, 'start')
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        desktop = client.desktop.find(args.desktop_id)
        client.desktop.start(desktop.desktop_id)
        return "done"


class StopDesktop(command.Command):
    _description = _("Stop desktop")

    def get_parser(self, prog_name):
        parser = super(StopDesktop, self).get_parser(prog_name)
        pb.DesktopParser.add_desktop_id_arg(parser, 'stop')
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        desktop = client.desktop.find(args.desktop_id)
        client.desktop.stop(desktop.desktop_id)
        return "done"


class DeleteDesktop(command.Command):
    _description = _("Delete desktop")

    def get_parser(self, prog_name):
        parser = super(DeleteDesktop, self).get_parser(prog_name)
        pb.DesktopParser.add_desktop_id_arg(parser, 'delete')
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        desktop = client.desktop.find(args.desktop_id)
        client.desktop.delete(desktop.desktop_id)
        return "done"


class EditDesktop(command.Command):
    # TODO (woo) 404
    _description = _("Edit desktop meta properties")

    def get_parser(self, prog_name):
        parser = super(EditDesktop, self).get_parser(prog_name)
        pb.DesktopParser.add_desktop_id_arg(parser, 'edit')
        pb.DesktopParser.add_edit_computer_name_option(parser, True)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        desktop = client.desktop.find(args.desktop_id)
        client.desktop.edit(desktop.desktop_id, args.computer_name)
        return args


class ShowDesktop(command.ShowOne):
    _description = _("Show desktop detail")

    def get_parser(self, prog_name):
        parser = super(ShowDesktop, self).get_parser(prog_name)
        pb.DesktopParser.add_desktop_id_arg(parser, 'show')
        return parser

    def take_action(self, args):
        compute = self.app.client_manager.compute
        client = self.app.client_manager.workspace
        desktop = client.desktop.find(args.desktop_id)
        # replace security groups
        sg_list = [utils.find_resource(compute.security_groups, sg['id']).name
                   for sg in desktop.security_groups]
        desktop.security_groups = sg_list

        columns = resource.Desktop.show_column_names
        formatter = resource.Desktop.formatter
        return columns, desktop.get_display_data(columns, formatter=formatter)
