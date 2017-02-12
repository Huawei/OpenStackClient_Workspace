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
import mock

from osc_lib import utils

from workspaceclient.osc.v1 import policy
from workspaceclient.tests import base
from workspaceclient.v1 import policy_mgr
from workspaceclient.v1 import resource


class TestPolicy(base.WorkspaceV1BaseTestCase):
    """"""

    instance = {
        "usb_port_redirection": {
            "enable": True,
            "options": {
                "usb_image_enable": False,
                "usb_video_enable": True,
                "usb_printer_enable": False,
                "usb_storage_enable": True,
                "usb_smart_card_enable": False
            }
        },
        "printer_redirection": {
            "enable": True,
            "options": {
                "sync_client_default_printer_enable": False,
                "universal_printer_driver": "Universal Printing PCL 6"
            }
        },
        "file_redirection": {
            "redirection_mode": "READ_AND_WRITE",
            "options": {
                "fixed_drive_enable": True,
                "removable_drive_enable": False,
                "cd_rom_drive_enable": True,
                "network_drive_enable": True
            }
        },
        "clipboard_redirection": "TWO_WAY_ENABLED",
        "hdp_plus": {
            "hdp_plus_enable": False,
            "display_level": "QUALITY_FIRST",
            "options": {
                "bandwidth": 24315,
                "frame_rate": 18,
                "video_frame_rate": 20,
                "smoothing_factor": 58,
                "lossy_compression_quality": 88
            }
        }
    }

    def __init__(self, *args, **kwargs):
        super(TestPolicy, self).__init__(*args, **kwargs)
        self._policy = None

    def setUp(self):
        super(TestPolicy, self).setUp()
        self._policy = resource.Policy(None, self.instance, attached=True)


class TestPolicyShow(TestPolicy):
    def setUp(self):
        super(TestPolicyShow, self).setUp()
        self.cmd = policy.ShowPolicy(self.app, None)

    @mock.patch.object(policy_mgr.PolicyManager, "_get")
    def test_desktop_show_with_computer_name(self, mocked_get):

        mocked_get.return_value = self._policy
        columns, data = self.cmd.take_action(None)

        expect_data = ('Enabled', 'Disabled', 'Enabled', 'Disabled', 'Enabled', 'Disabled')
        self.assertEqual(expect_data, data)



        # self.assertEqual(columns, resource.AntiDDos.list_column_names)
        # self.assertEqual(data, antiddos_list[0].get_display_data(columns))

        # @mock.patch.object(policy_mgr.DesktopManager, "_list")
        # def test_antiddos_find_return_single_result(self, mocked_find):
        #     ip = "192.168.42.221"
        #     args = [ip]
        #     verify_args = [("floating_ip", ip), ]
        #     parsed_args = self.check_parser(self.cmd, args, verify_args)
        #
        #     antiddos_list = self.get_fake_antiddos_list(1)
        #     mocked_find.return_value = antiddos_list
        #     columns, data = self.cmd.take_action(parsed_args)
        #     mocked_find.assert_called_once_with(
        #         "/antiddos", params={"ip": ip}, key='ddosStatus'
        #     )
        #     self.assertEqual(columns, resource.AntiDDos.list_column_names)
        #     self.assertEqual(data, antiddos_list[0].get_display_data(columns))
        #
        # @mock.patch.object(policy_mgr.DesktopManager, "_list")
        # def test_antiddos_show_multiple_ip_matched(self, mocked_find):
        #     ip = "192.168.42.22"
        #     args = [ip]
        #     verify_args = [("floating_ip", ip), ]
        #     parsed_args = self.check_parser(self.cmd, args, verify_args)
        #     mocked_find.return_value = self.get_fake_antiddos_list()
        #     self.assertRaises(
        #         exceptions.NotUniqueMatch, self.cmd.take_action, parsed_args
        #     )
        #
        # @mock.patch.object(policy_mgr.DesktopManager, "_get")
        # def test_antiddos_show_with_id(self, mocked_get):
        #     _antiddos = self.get_fake_desktop()
        #     floating_ip_id = _antiddos.floating_ip_id
        #     verify_args = [("floating_ip", floating_ip_id), ]
        #     parsed_args = self.check_parser(
        #         self.cmd, [floating_ip_id], verify_args
        #     )
        #
        #     mocked_get.return_value = _antiddos
        #     columns, data = self.cmd.take_action(parsed_args)
        #     mocked_get.assert_called_once_with(
        #         "/antiddos/" + floating_ip_id
        #     )
        #     self.assertEqual(columns, resource.AntiDDos.list_column_names)
        #     self.assertEqual(data, _antiddos.get_display_data(columns))
        #
        # @mock.patch.object(policy_mgr.DesktopManager, "_list")
        # def test_antiddos_show_not_found_raised(self, mocked_find):
        #     ip = "10.10.10.10"
        #     args = [ip]
        #     verify_args = [("floating_ip", ip), ]
        #     parsed_args = self.check_parser(self.cmd, args, verify_args)
        #     mocked_find.return_value = base_resource.TupleWithMeta([], "RID")
        #     self.assertRaises(
        #         execs.NotFound, self.cmd.take_action, parsed_args
        #     )
