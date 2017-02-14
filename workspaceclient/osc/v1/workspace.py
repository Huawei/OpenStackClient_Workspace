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
from workspaceclient.v1 import resource

LOG = logging.getLogger(__name__)


class CreateWorkspace(command.Command):
    _description = _("create workspace")

    def get_parser(self, prog_name):
        parser = super(CreateWorkspace, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        products = client.workspaces.list()
        columns = resource.Product.list_column_names
        outputs = [r.get_display_data(columns) for r in products]
        return columns, outputs


class ShowWorkspace(command.ShowOne):
    _description = _("show workspace")

    def get_parser(self, prog_name):
        parser = super(ShowWorkspace, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        workspace = client.workspaces.get()
        columns = resource.Workspace.show_column_names
        outputs = workspace.get_display_data(columns)
        return columns, outputs


class EditWorkspace(command.Command):
    _description = _("show workspace")

    def get_parser(self, prog_name):
        parser = super(ShowWorkspace, self).get_parser(prog_name)

        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        products = client.workspaces.list()
        columns = resource.Product.list_column_names
        outputs = [r.get_display_data(columns) for r in products]
        return columns, outputs


class DeleteWorkspace(command.ShowOne):
    _description = _("show workspace")

    def get_parser(self, prog_name):
        parser = super(ShowWorkspace, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        products = client.workspaces.list()
        columns = resource.Product.list_column_names
        outputs = [r.get_display_data(columns) for r in products]
        return columns, outputs
