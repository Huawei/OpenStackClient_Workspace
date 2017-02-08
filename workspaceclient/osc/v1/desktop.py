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

from workspaceclient.common import parser as p
from workspaceclient.common.i18n import _
from workspaceclient.osc.v1 import parser_builder as pb
from workspaceclient.v1 import resource

LOG = logging.getLogger(__name__)


class ListDesktop(command.Lister):
    _description = _("list desktops")

    def get_parser(self, prog_name):
        parser = super(ListDesktop, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.workspace
        desktops = client.desktop.list()
        columns = resource.Desktop.list_column_names
        data = [r.get_display_data(columns) for r in desktops]
        return columns, data


