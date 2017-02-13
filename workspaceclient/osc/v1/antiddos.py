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

from workspaceclient.common import parser_builder as p
from workspaceclient.common.i18n import _
from workspaceclient.osc.v1 import parser_builder as pb
from workspaceclient.v1 import resource

LOG = logging.getLogger(__name__)


class QueryAntiDDosConfig(command.Lister):
    _description = _("Query AntiDDos configurations")

    def get_parser(self, prog_name):
        parser = super(QueryAntiDDosConfig, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.antiddos
        data = client.antiddos.query_config_list()
        columns = resource.AntiDDos.list_column_names
        return columns, (r.get_display_data(columns) for r in data)


class OpenAntiDDos(command.Command):
    _description = _("Open AntiDDos for floating IP")

    def get_parser(self, prog_name):
        parser = super(OpenAntiDDos, self).get_parser(prog_name)
        pb.DesktopParser.add_floating_ip_arg(parser)
        pb.DesktopParser.add_enable_l7_arg(parser)
        pb.DesktopParser.add_traffic_pos_arg(parser)
        pb.DesktopParser.add_http_request_pos_arg(parser)
        pb.DesktopParser.add_cleaning_access_pos_arg(parser)
        pb.DesktopParser.add_app_type_arg(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.antiddos
        floating_ip = client.antiddos.find(args.floating_ip)
        task = client.antiddos.open_antiddos(floating_ip.floating_ip_id,
                                             args.enable_l7,
                                             args.traffic_pos,
                                             args.http_request_pos,
                                             args.cleaning_access_pos,
                                             args.app_type)

        return 'Request Received, task id: ' + task['task_id']


class CloseAntiDDos(command.Command):
    _description = _("Close AntiDDos of floating IP")

    def get_parser(self, prog_name):
        parser = super(CloseAntiDDos, self).get_parser(prog_name)
        pb.DesktopParser.add_floating_ip_arg(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.antiddos
        floating_ip = client.antiddos.find(args.floating_ip)
        task = client.antiddos.close_antiddos(floating_ip.floating_ip_id)
        return 'Request Received, task id: ' + task['task_id']


class ShowAntiDDos(command.ShowOne):
    _description = _("Display AntiDDos settings of floating IP")

    def get_parser(self, prog_name):
        parser = super(ShowAntiDDos, self).get_parser(prog_name)
        pb.DesktopParser.add_floating_ip_arg(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.antiddos
        _antiddos = client.antiddos.find(args.floating_ip)
        columns = resource.AntiDDos.list_column_names
        return columns, _antiddos.get_display_data(columns)


class SetAntiDDos(command.Command):
    _description = _("Set AntiDDos settings of floating IP")

    def get_parser(self, prog_name):
        parser = super(SetAntiDDos, self).get_parser(prog_name)
        pb.DesktopParser.add_floating_ip_arg(parser)
        pb.DesktopParser.add_enable_l7_arg(parser)
        pb.DesktopParser.add_traffic_pos_arg(parser)
        pb.DesktopParser.add_http_request_pos_arg(parser)
        pb.DesktopParser.add_cleaning_access_pos_arg(parser)
        pb.DesktopParser.add_app_type_arg(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.antiddos
        floating_ip = client.antiddos.find(args.floating_ip)
        task = client.antiddos.update_antiddos(floating_ip.floating_ip_id,
                                               args.enable_l7,
                                               args.traffic_pos,
                                               args.http_request_pos,
                                               args.cleaning_access_pos,
                                               args.app_type)
        return 'Request Received, task id: ' + task['task_id']


class ShowAntiDDosTask(command.ShowOne):
    _description = _("Display AntiDDos setting task")

    def get_parser(self, prog_name):
        parser = super(ShowAntiDDosTask, self).get_parser(prog_name)
        parser.add_argument(
            'task_id',
            metavar='<task id>',
            help=_("AntiDDos setting task id")
        )
        return parser

    def take_action(self, args):
        client = self.app.client_manager.antiddos
        task = client.antiddos.get_task_status(args.task_id)
        columns = resource.AntiDDosTask.show_column_names
        return columns, task.get_display_data(columns)


class ListAntiDDosStatus(command.Lister):
    _description = _("List AntiDDos status")

    def get_parser(self, prog_name):
        parser = super(ListAntiDDosStatus, self).get_parser(prog_name)
        parser.add_argument(
            "--status",
            choices=resource.AntiDDos.status_list,
            help=_("list AntiDDos with status")
        )
        parser.add_argument(
            "--ip",
            help=_("list AntiDDos with the ip (eg: 110.110.)")
        )
        p.BaseParser.add_limit_option(parser)
        p.BaseParser.add_offset_option(parser)
        return parser

    def take_action(self, args):
        client = self.app.client_manager.antiddos
        data = client.antiddos.list(status=args.status,
                                    ip=args.ip,
                                    limit=args.limit,
                                    offset=args.offset)
        columns = resource.AntiDDos.list_column_names
        return columns, (r.get_display_data(columns) for r in data)


class ShowAntiDDosStatus(command.ShowOne):
    _description = _("Display AntiDDos status of floating ip")

    def get_parser(self, prog_name):
        parser = super(ShowAntiDDosStatus, self).get_parser(prog_name)
        pb.DesktopParser.add_floating_ip_arg(parser)
        return parser

    def take_action(self, args):
        manager = self.app.client_manager.antiddos.antiddos
        floating_ip = manager.find(args.floating_ip)
        status = manager.get_antiddos_status(floating_ip.floating_ip_id)
        columns = resource.AntiDDosStatus.show_column_names
        return columns, status.get_display_data(columns)


class ListAntiDDosDailyReport(command.Lister):
    _description = _("List AntiDDos report(every 5min) of past 24h")

    def get_parser(self, prog_name):
        parser = super(ListAntiDDosDailyReport, self).get_parser(prog_name)
        pb.DesktopParser.add_floating_ip_arg(parser)
        return parser

    def take_action(self, args):
        manager = self.app.client_manager.antiddos.antiddos
        floating_ip = manager.find(args.floating_ip)
        reports = manager.get_antiddos_daily_report(floating_ip.floating_ip_id)
        columns = resource.AntiDDosDailyReport.list_column_names
        return columns, (r.get_display_data(columns) for r in reports)


class ListAntiDDosLogs(command.Lister):
    _description = _("List AntiDDos logs(every 5min) of past 24h")

    def get_parser(self, prog_name):
        parser = super(ListAntiDDosLogs, self).get_parser(prog_name)
        pb.DesktopParser.add_floating_ip_arg(parser)
        p.BaseParser.add_limit_option(parser)
        p.BaseParser.add_offset_option(parser)
        p.BaseParser.add_sortdir_option(parser)
        return parser

    def take_action(self, args):
        # TODO(Woo) no data in test env, need to test later
        manager = self.app.client_manager.antiddos.antiddos
        floating_ip = manager.find(args.floating_ip)
        logs = manager.get_antiddos_daily_logs(
            floating_ip.floating_ip_id, args.sort_dir, args.limit, args.offset
        )
        columns = resource.AntiDDosLog.list_column_names
        data = (r.get_display_data(columns, formatter=r.formatter)
                for r in logs)
        return columns, data


class ListAntiDDosWeeklyReport(command.Lister):
    _description = _("List AntiDDos weekly report")

    def get_parser(self, prog_name):
        # TODO (woo)
        parser = super(ListAntiDDosWeeklyReport, self).get_parser(prog_name)
        parser.add_argument(
            '--start-date',
            metavar='<start-date>',
            required=True,
            help=_("start date, start ")
        )
        return parser

    def take_action(self, args):
        manager = self.app.client_manager.antiddos.antiddos
        floating = manager.find(args.floating_ip)
        floating_ip_id = floating.floating_ip_id
        reports = manager.get_antiddos_weekly_report(floating_ip_id)
        columns = resource.AntiDDosWeeklyReport.list_column_names
        return columns, (r.get_display_data(columns) for r in reports)
