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

    # @mock.patch.object(utils, "find_resource")
    @mock.patch.object(desktop_mgr.DesktopManager, "find")
    def test_desktop_show_with_computer_name(self, mocked_find):
        computer_name = "cm01"
        args = [computer_name]
        verify_args = [("desktop_id", computer_name), ]
        parsed_args = self.check_parser(self.cmd, args, verify_args)

        # mocked_resource.side_effect = [
        #     base_resource.Resource(None, dict(name='sg01')),
        #     base_resource.Resource(None, dict(name='sg02')),
        # ]

        _desktop = self.get_fake_desktop(instance=self.instances[0])
        mocked_find.return_value = _desktop
        columns, data = self.cmd.take_action(parsed_args)

        show_column_names = [
            "Desktop Id",
            "Computer Name",
            "User Name",
            "Product Id",
            "Security Groups",
            "Flavor",
            "metadata",
            "addresses",
            "Root Volume",
            "Data Volumes",
            "Created",
            "Login Status",
            "Status"
        ]

        sg_list = ", ".join([
            '46946f87-ccf7-4be2-ac1d-8b6a18deb77b',
            '46946f87-ccf7-4be2-ac1d-8b6a18deb77c',
        ])

        expect_data = (
            'f77db5cd-c020-47d4-bbbe-9b979a38d18c', 'cm01', 'cm',
            'workspace.c2.large.windows', sg_list, 'computev2-2',
            ("charging_mode='0', image_name='workspace-user-template-test', "
             "metering.cloudServiceType='sys.service.type.ec2', "
             "metering.image_id='3a6886dc-fede-4cc9-bc19-39a3f4a9c31e', "
             "metering.imagetype='private', "
             "metering.resourcespeccode='c2.large.win', "
             "metering.resourcetype='1', os_bit='64', os_type='Windows', "
             "vpc_id='bd44b40c-4491-4d76-8ffb-0d86c094eacc'"),
            ("OS-EXT-IPS-MAC:mac_addr='fa:16:3e:81:e6:ad', "
             "OS-EXT-IPS:type='fixed', addr='192.168.0.22', version='4'\n"
             "OS-EXT-IPS-MAC:mac_addr='fa:16:3e:a7:1c:ca', "
             "OS-EXT-IPS:type='fixed', addr='172.16.0.25', version='4'"),
            "size='80', type='SATA'", "size='10', type='SATA'",
            '2016-11-14T14:41:25.000Z', 'REGISTERED', 'ACTIVE'
        )
        self.assertEquals(show_column_names, columns)
        self.assertEqual(expect_data, data)


class TestDesktopList(TestDesktop):
    def setUp(self):
        super(TestDesktopList, self).setUp()
        self.cmd = desktop.ListDesktop(self.app, None)

    @mock.patch.object(desktop_mgr.DesktopManager, "_list")
    def test_desktop_list(self, mocked_list):
        args = [
            "--status", "ACTIVE",
            "--desktop-ip", "10.10.10.10",
            "--user-name", "user01",
            "--computer-name", "computer01",
            "--marker", "desktop-id",
            "--limit", "10",
        ]
        verify_args = [
            ("status", "ACTIVE"),
            ("desktop_ip", "10.10.10.10"),
            ("user_name", "user01"),
            ("computer_name", "computer01"),
            ("marker", "desktop-id"),
            ("limit", 10),
        ]
        parsed_args = self.check_parser(self.cmd, args, verify_args)

        desktops = [
            {
                "desktop_id": "f41fb23a-376e-475d-bcaa-8e9f827aad62",
                "computer_name": "hyqvm101",
                "created": "2016-10-08T06:44:57.000Z",
                "ip_address": "192.168.0.139",
                "user_name": "hyqvm1"
            },
            {
                "desktop_id": "b94a88e9-b67d-40d3-a3be-d207826ffdf2",
                "computer_name": "huangyq301",
                "created": "2016-10-06T11:39:22.000Z",
                "ip_address": "192.168.0.34",
                "user_name": "huangyq3"
            }
        ]

        mocked_list.return_value = [resource.Desktop(None, d, attached=True)
                                    for d in desktops]
        columns, data = self.cmd.take_action(parsed_args)

        params = {
            "status": "ACTIVE",
            "desktop_ip": "10.10.10.10",
            "user_name": "user01",
            "computer_name": "computer01",
            "marker": "desktop-id",
            "limit": 10,
        }

        mocked_list.assert_called_once_with("/desktops",
                                            params=params,
                                            key='desktops')

        self.assertEquals(resource.Desktop.list_column_names, columns)
        expected = [('f41fb23a-376e-475d-bcaa-8e9f827aad62', 'hyqvm101',
                     'hyqvm1', '192.168.0.139', '2016-10-08T06:44:57.000Z'),
                    ('b94a88e9-b67d-40d3-a3be-d207826ffdf2', 'huangyq301',
                     'huangyq3', '192.168.0.34', '2016-10-06T11:39:22.000Z')]
        self.assertEquals(expected, data)
