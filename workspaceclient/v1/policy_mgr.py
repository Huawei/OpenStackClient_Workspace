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
from keystoneauth1 import exceptions

from workspaceclient.common import exceptions as execs
from workspaceclient.common import manager
from workspaceclient.common import utils
from workspaceclient.common.i18n import _
from workspaceclient.v1 import resource


class PolicyManager(manager.Manager):
    """Policy API management"""

    resource_class = resource.Policy

    def get(self):
        return self._get("/policies", key="policies")

    def edit(self):
        # {
        #     "policies": {
        #         "usb_port_redirection": {
        #             "enable": false,
        #             "options": {
        #                 "usb_image_enable": false,
        #                 "usb_video_enable": true,
        #                 "usb_printer_enable": false,
        #                 "usb_storage_enable": true,
        #                 "usb_smart_card_enable": false
        #             }
        #         },
        #         "printer_redirection": {
        #             "enable": true,
        #             "options": {
        #                 "sync_client_default_printer_enable": false,
        #                 "universal_printer_driver": "Universal Printing PCL 6"
        #             }
        #         },
        #         "file_redirection": {
        #             "redirection_mode": "READ_AND_WRITE",
        #             "options": {
        #                 "fixed_drive_enable": true,
        #                 "removable_drive_enable": false,
        #                 "cd_rom_drive_enable": true,
        #                 "network_drive_enable": true
        #             }
        #         },
        #         "clipboard_redirection": "TWO_WAY_ENABLED",
        #         "hdp_plus": {
        #             "hdp_plus_enable": false,
        #             "display_level": "QUALITY_FIRST",
        #             "options": {
        #                 "bandwidth": 24315,
        #                 "frame_rate": 18,
        #                 "video_frame_rate": 20,
        #                 "smoothing_factor": 58,
        #                 "lossy_compression_quality": 88
        #             }
        #         }
        #     }
        # }

        return self._update_all("/policies")
