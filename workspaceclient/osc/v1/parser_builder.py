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
from workspaceclient.common import parsetypes
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


class PolicyParser(object):

    @staticmethod
    def add_switch_arg(parser, name, required=False):
        group = parser.add_mutually_exclusive_group(required=required)
        group.add_argument(
            '--enable-%s' % name,
            action="store_true",
            default=None,
            dest='enable_%s' % name.replace("-", "_"),
            help=_("enable %s" % name.replace("-", " "))
        )
        group.add_argument(
            '--disable-%s' % name,
            action="store_false",
            default=None,
            dest='enable_%s' % name.replace("-", "_"),
            help=_("disable %s" % name.replace("-", " "))
        )

    @staticmethod
    def add_printer_driver_arg(parser):
        parser.add_argument(
            "--universal-printer-driver",
            choices=[
                "Default",
                "HDP XPSDrv Driver",
                "Universal Printing PCL 5",
                "Universal Printing PCL 6",
                "Universal Printing PS"
            ],
            help=_("setup universal printer driver")
        )

    @staticmethod
    def add_file_redirection_mode_arg(parser):
        parser.add_argument(
            "--file-redirection-mode",
            choices=[
                "DISABLED",
                "READ_ONLY",
                "READ_AND_WRITE",
            ],
            help=_("setup file redirection mode")
        )

    @staticmethod
    def add_clipboard_redirection_arg(parser):
        parser.add_argument(
            "--clipboard-redirection",
            choices=[
                "DISABLED",
                "SERVER_TO_CLIENT_ENABLED",
                "CLIENT_TO_SERVER_ENABLED",
                "TWO_WAY_ENABLED",
            ],
            help=_("setup clipboard redirection")
        )

    @staticmethod
    def add_display_level_arg(parser):
        parser.add_argument(
            "--display-level",
            choices=[
                "SMOOTHNESS_FIRST",
                "QUALITY_FIRST",
            ],
            help=_("display level")
        )

    @staticmethod
    def add_bandwidth_arg(parser):
        parser.add_argument(
            "--bandwidth",
            metavar="<Kbps>",
            type=parsetypes.int_range_type(1000, 25000),
            help=_("Bandwidth, value range is [1000-25000]")
        )

    @staticmethod
    def add_frame_rate_arg(parser):
        parser.add_argument(
            "--frame-rate",
            metavar="<FPS>",
            type=parsetypes.int_range_type(15, 30),
            help=_("Frame rate, value range is [15-30]")
        )

    @staticmethod
    def add_video_frame_rate_arg(parser):
        parser.add_argument(
            "--video-frame-rate",
            metavar="<FPS>",
            type=parsetypes.int_range_type(15, 50),
            help=_("Video frame rate, value range is [15-50]")
        )

    @staticmethod
    def add_smoothing_factor_arg(parser):
        parser.add_argument(
            "--smoothing-factor",
            metavar="<smoothing-factor>",
            type=parsetypes.int_range_type(0, 60),
            help=_("Video frame rate, value range is [0-60]")
        )

    @staticmethod
    def add_lossy_compression_quality_arg(parser):
        parser.add_argument(
            "--lossy-compression-quality",
            metavar="<quality>",
            type=parsetypes.int_range_type(70, 90),
            help=_("lossy compression quality, value range is [70-90]")
        )


class DesktopUserParser(object):

    @staticmethod
    def add_username_option(parser):
        parser.add_argument(
            "--user-name",
            metavar="<user-name>",
            help=_("list desktop users with name")
        )

    @staticmethod
    def add_email_option(parser):
        parser.add_argument(
            "--user-email",
            metavar="<user-email>",
            help=_("list desktop users with email")
        )

    @staticmethod
    def add_marker_option(parser):
        parser.add_argument(
            "--marker",
            metavar="<user-name>",
            help=_("The last user-name of the previous page")
        )

    @staticmethod
    def add_start_time_option(parser):
        parser.add_argument(
            "--start-time",
            metavar="<yyyy-MM-dd HH:mm>",
            type=parsetypes.date_type('%Y-%m-%d %H:%M'),
            help=_("list login records after the UTC time")
        )

    @staticmethod
    def add_end_time_option(parser):
        parser.add_argument(
            "--end-time",
            metavar="<yyyy-MM-dd HH:mm>",
            type=parsetypes.date_type('%Y-%m-%d %H:%M'),
            help=_("list login records before the UTC time")
        )

    @staticmethod
    def add_computer_name_option(parser, required=False):
        parser.add_argument(
            "--computer-name",
            metavar="<computer-name>",
            required=required,
            help=_("list login records for desktop with computer name")
        )

    @staticmethod
    def add_user_name_option(parser, required=False):
        parser.add_argument(
            "--user-name",
            metavar="<user-name>",
            required=required,
            help=_("list login records which login with user-name")
        )

    @staticmethod
    def add_terminal_type_option(parser, required=False):
        parser.add_argument(
            "--terminal-type",
            metavar="<terminal-type>",
            required=required,
            help=_("list login records which login from terminal type")
        )
