#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from workspaceclient.common import utils
from workspaceclient.common.i18n import _


class DesktopParser(object):
    @staticmethod
    def add_floating_ip_arg(parser):
        parser.add_argument(
            'floating_ip',
            metavar='<floating ip>',
            help=_("For floating ip (UUID or IP)")
        )

    @staticmethod
    def add_enable_l7_arg(parser):
        enable_group = parser.add_mutually_exclusive_group()
        enable_group.add_argument(
            '--enable-l7',
            action="store_true",
            dest='enable_l7',
            default=True,
            help=_("enable L7 protection (default)")
        )
        enable_group.add_argument(
            '--disable-l7',
            action="store_false",
            dest='enable_l7',
            help=_("disable L7 protection")
        )

    @staticmethod
    def add_traffic_pos_arg(parser):
        parser.add_argument(
            '--traffic-pos',
            required=True,
            choices=utils.str_range(1, 10),
            help=_("traffic pos, integer between 1-9")
        )

    @staticmethod
    def add_http_request_pos_arg(parser):
        parser.add_argument(
            '--http-request-pos',
            required=True,
            choices=utils.str_range(1, 16),
            help=_("http request pos, integer between 1-15")
        )

    @staticmethod
    def add_cleaning_access_pos_arg(parser):
        parser.add_argument(
            '--cleaning-access-pos',
            required=True,
            choices=utils.str_range(1, 9),
            help=_("cleaning access pos, integer between 1-8")
        )

    @staticmethod
    def add_app_type_arg(parser):
        parser.add_argument(
            '--app-type',
            required=True,
            choices=('0', '1'),
            help=_("app type, 0 or 1")
        )
