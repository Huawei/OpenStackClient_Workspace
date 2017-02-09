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
from workspaceclient.common.i18n import _


class DesktopParser(object):
    @staticmethod
    def add_desktop_id_arg(parser, op):
        parser.add_argument(
            "desktop_id",
            metavar="<desktop>",
            help=_("Desktop to %s (desktop-id or computer-name)" % op)
        )

    @staticmethod
    def add_hard_or_soft_arg(parser, required=True):
        force_reboot = parser.add_mutually_exclusive_group(required=required)
        force_reboot.add_argument(
            '--hard',
            action="store_true",
            dest='force',
            default=False,
            help=_("hard reboot")
        )
        force_reboot.add_argument(
            '--soft',
            action="store_false",
            dest='force',
            default=False,
            help=_("soft reboot")
        )

    @staticmethod
    def add_status_option(parser):
        parser.add_argument(
            "--status",
            choices=["ACTIVE", "SHUTOFF", "ERROR"],
            help=_("list desktop with status")
        )

    @staticmethod
    def add_desktop_ip_option(parser):
        parser.add_argument(
            "--desktop-ip",
            metavar="<desktop-ip>",
            help=_("list desktop with the ip")
        )

    @staticmethod
    def add_user_name_option(parser):
        parser.add_argument(
            "--user-name",
            metavar="<user-name>",
            help=_("list desktop with the user name")
        )

    @staticmethod
    def add_computer_name_option(parser, required=False):
        parser.add_argument(
            "--computer-name",
            metavar="<computer-name>",
            required=required,
            help=_("list desktop with the computer name")
        )

    @staticmethod
    def add_marker_option(parser):
        parser.add_argument(
            "--marker",
            metavar="<desktop-id>",
            help=_("The last desktop ID of the previous page")
        )

    @staticmethod
    def add_edit_computer_name_option(parser, required=True):
        parser.add_argument(
            "--computer-name",
            metavar="<computer-name>",
            required=required,
            help=_("Change computer name to (must be unique, "
                   "[a-zA-Z0-9-_] allowed, start with [a-zA-Z])")
        )
