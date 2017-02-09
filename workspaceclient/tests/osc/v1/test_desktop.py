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
import random
import mock

from osc_lib import utils

from workspaceclient.common import resource as base_resource
from workspaceclient.osc.v1 import desktop
from workspaceclient.tests import base
from workspaceclient.v1 import desktop_mgr
from workspaceclient.v1 import resource


class TestDesktop(base.WorkspaceV1BaseTestCase):
    """"""

    instances = [{
        "desktop_id": "f77db5cd-c020-47d4-bbbe-9b979a38d18c",
        "computer_name": "cm01",
        "status": "ACTIVE",
        "created": "2016-11-14T14:41:25.000Z",
        "login_status": "REGISTERED",
        "user_name": "cm",
        "security_groups": [{
            "id": "46946f87-ccf7-4be2-ac1d-8b6a18deb77b"
        }, {
            "id": "46946f87-ccf7-4be2-ac1d-8b6a18deb77c"
        }],
        "flavor": {
            "id": "computev2-2",
            "links": [{
                "rel": "bookmark",
                "hrel": "https://compute.region.eu-de.otc-tsi.de/b99add77e7924466852c793e041a7d6a/flavors/computev2-2"
            }]
        },
        "metadata": {
            "metering.image_id": "3a6886dc-fede-4cc9-bc19-39a3f4a9c31e",
            "metering.imagetype": "private",
            "metering.resourcespeccode": "c2.large.win",
            "metering.cloudServiceType": "sys.service.type.ec2",
            "image_name": "workspace-user-template-test",
            "metering.resourcetype": "1",
            "os_bit": "64",
            "vpc_id": "bd44b40c-4491-4d76-8ffb-0d86c094eacc",
            "os_type": "Windows",
            "charging_mode": "0"
        },
        "addresses": {
            "aa60ef37-e2b1-4a25-b2f7-077592c060fa": [{
                "addr": "192.168.0.22",
                "version": 4,
                "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:81:e6:ad",
                "OS-EXT-IPS:type": "fixed"
            }],
            "bd44b40c-4491-4d76-8ffb-0d86c094eacc": [{
                "addr": "172.16.0.25",
                "version": 4,
                "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:a7:1c:ca",
                "OS-EXT-IPS:type": "fixed"
            }
            ]
        },
        "product_id": "workspace.c2.large.windows",
        "root_volume": {
            "type": "SATA",
            "size": 80
        },
        "data_volumes": [{
            "type": "SATA",
            "size": 10
        }]
    }, {
        "desktop_id": "7dbc9fbb-447a-4180-9f86-70951646d8a5",
        "computer_name": "chen01",
        "status": "SHUTOFF",
        "created": "2016-11-11T06:59:41.000Z",
        "login_status": "UNREGISTER",
        "user_name": "chen",
        "security_groups": [{
            "id": "46946f87-ccf7-4be2-ac1d-8b6a18deb77b"
        }],
        "flavor": {
            "id": "computev2-4",
            "links": [{
                "rel": "bookmark",
                "hrel": "https://compute.region.eu-de.otc-tsi.de/b99add77e7924466852c793e041a7d6a/flavors/computev2-4"
            }]
        },
        "metadata": {
            "metering.image_id": "9a07cffa-7294-49f6-a795-f3db306a4b5a",
            "metering.imagetype": "private",
            "metering.resourcespeccode": "c2.2xlarge.win",
            "metering.cloudServiceType": "sys.service.type.ec2",
            "image_name": "workspace-user-template0809",
            "metering.resourcetype": "1",
            "os_bit": "64",
            "vpc_id": "bd44b40c-4491-4d76-8ffb-0d86c094eacc",
            "os_type": "Windows",
            "charging_mode": "0"
        },
        "addresses": {
            "aa60ef37-e2b1-4a25-b2f7-077592c060fa": [{
                "addr": "192.168.0.20",
                "version": 4,
                "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:09:7b:c4",
                "OS-EXT-IPS:type": "fixed"
            }],
            "bd44b40c-4491-4d76-8ffb-0d86c094eacc": [{
                "addr": "172.16.0.23",
                "version": 4,
                "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:2b:da:23",
                "OS-EXT-IPS:type": "fixed"
            }]
        },
        "product_id": "workspace.c2.2xlarge.windows",
        "root_volume": {
            "type": "SATA",
            "size": 80
        },
        "data_volumes": [{
            "type": "SATA",
            "size": 20
        }]
    }]

    def get_fake_desktop_list(self, count=0):
        if count == 0:
            results = [resource.Desktop(None, instance, attached=True)
                       for instance in self.instances]
        else:
            results = [resource.Desktop(None, instance, attached=True)
                       for instance in self.instances[:count]]
        return base_resource.ListWithMeta(results, "Request-Id")

    def get_fake_desktop(self, instance=None):
        if instance:
            _desktop = resource.Desktop(None, instance, attached=True)
        else:
            seed = random.randint(0, len(self.instances) - 1)
            _desktop = resource.Desktop(
                None, self.instances[seed], attached=True
            )
        return _desktop

    def __init__(self, *args, **kwargs):
        super(TestDesktop, self).__init__(*args, **kwargs)
        self._desktop = None
        self.mocked_find = None

    def setUp(self):
        super(TestDesktop, self).setUp()
        self._desktop = self.get_fake_desktop()
        self.mocked_find = mock.patch.object(
            desktop_mgr.DesktopManager, "find", return_value=self._desktop
        )


class TestDesktopShow(TestDesktop):
    def setUp(self):
        super(TestDesktopShow, self).setUp()
        self.cmd = desktop.ShowDesktop(self.app, None)

    @mock.patch.object(utils, "find_resource")
    @mock.patch.object(desktop_mgr.DesktopManager, "find")
    def test_desktop_show_with_computer_name(self, mocked_find,
                                             mocked_resource):
        computer_name = "cm01"
        args = [computer_name]
        verify_args = [("desktop_id", computer_name), ]
        parsed_args = self.check_parser(self.cmd, args, verify_args)

        mocked_resource.side_effect = [
            base_resource.Resource(None, dict(name='sg01')),
            base_resource.Resource(None, dict(name='sg02')),
        ]

        desktop = self.get_fake_desktop(instance=self.instances[0])
        mocked_find.return_value = desktop
        columns, data = self.cmd.take_action(parsed_args)

        expect_data = (
            'f77db5cd-c020-47d4-bbbe-9b979a38d18c', 'cm01', 'cm',
            'workspace.c2.large.windows', 'sg01, sg02',
            '2016-11-14T14:41:25.000Z', 'REGISTERED', 'ACTIVE'
        )

        self.assertEqual(data, expect_data)



        # self.assertEqual(columns, resource.AntiDDos.list_column_names)
        # self.assertEqual(data, antiddos_list[0].get_display_data(columns))

        # @mock.patch.object(desktop_mgr.DesktopManager, "_list")
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
        # @mock.patch.object(desktop_mgr.DesktopManager, "_list")
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
        # @mock.patch.object(desktop_mgr.DesktopManager, "_get")
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
        # @mock.patch.object(desktop_mgr.DesktopManager, "_list")
        # def test_antiddos_show_not_found_raised(self, mocked_find):
        #     ip = "10.10.10.10"
        #     args = [ip]
        #     verify_args = [("floating_ip", ip), ]
        #     parsed_args = self.check_parser(self.cmd, args, verify_args)
        #     mocked_find.return_value = base_resource.TupleWithMeta([], "RID")
        #     self.assertRaises(
        #         execs.NotFound, self.cmd.take_action, parsed_args
        #     )
