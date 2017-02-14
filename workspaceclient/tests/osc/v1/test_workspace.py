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
import mock

from workspaceclient.common import resource as base_resource
from workspaceclient.osc.v1 import workspace
from workspaceclient.tests import base
from workspaceclient.v1 import workspace_mgr


class TestWorkspaceEnable(base.WorkspaceV1BaseTestCase):
    def setUp(self):
        super(TestWorkspaceEnable, self).setUp()
        self.cmd = workspace.EnableWorkspace(self.app, None)

    @mock.patch.object(workspace_mgr.WorkspaceManager, "_create")
    def test_enable_lite_ad_workspace(self, mocked_create):
        args = [
            "--domain-type", "LITE_AD",
            "--domain-name", "test.com",
            "--domain-admin-account", "test",
            "--domain-password", "Test!@#$22",
            "--vpc", "vpc-name",
            "--subnet", "subnet-name-01",
            "--subnet", "subnet-name-02",
            "--access-mode", "INTERNET",
        ]
        verify_args = [
            ("domain_type", "LITE_AD"),
            ("domain_name", "test.com"),
            ("domain_admin_account", "test"),
            ("domain_password", "Test!@#$22"),
            ("vpc", "vpc-name"),
            ("subnets", ["subnet-name-01", "subnet-name-02", ]),
            ("access_mode", "INTERNET"),
        ]
        parsed_args = self.check_parser(self.cmd, args, verify_args)

        # mock return values
        _network = base_resource.Resource(None, dict(id="network-id"))
        self.app.client_manager.network.find_network.return_value = _network
        _subnets = [base_resource.Resource(None, dict(id="subnet-id-1")),
                    base_resource.Resource(None, dict(id="subnet-id-2"))]
        self.app.client_manager.network.find_subnet.side_effect = _subnets
        _job = base_resource.DictWithMeta(dict(job_id="job_id"), 'RID')
        mocked_create.return_value = _job

        # take cmd
        result = self.cmd.take_action(parsed_args)

        json = {
            "ad_domains": {
                "domain_type": "LITE_AD",
                "domain_name": "test.com",
                "domain_admin_account": "test",
                "domain_password": "Test!@#$22"
            },
            "vpc_id": "network-id",
            "subnet_ids": [{
                "subnet_id": "subnet-id-1"
            }, {
                "subnet_id": "subnet-id-2"
            }],
            "access_mode": "INTERNET"
        }

        mocked_create.assert_called_once_with(
            "/workspaces", json=json, raw=True
        )
        self.assertEqual("Request Received, job id: %s" % _job["job_id"],
                         result)

    @mock.patch.object(workspace_mgr.WorkspaceManager, "_create")
    def test_enable_local_ad_workspace(self, mocked_create):
        args = [
            "--domain-type", "LOCAL_AD",
            "--domain-name", "test.com",
            "--domain-admin-account", "test",
            "--domain-password", "Test!@#$22",
            "--active-domain-ip", "1.1.1.1",
            "--standby-domain-ip", "1.1.1.1",
            "--active-dns-ip", "1.1.1.1",
            "--standby-dns-ip", "1.1.1.1",
            "--vpc", "vpc-name",
            "--subnet", "subnet-name-01",
            "--subnet", "subnet-name-02",
            "--access-mode", "INTERNET",
        ]
        verify_args = [
            ("domain_type", "LOCAL_AD"),
            ("domain_name", "test.com"),
            ("domain_admin_account", "test"),
            ("domain_password", "Test!@#$22"),
            ("active_domain_ip", "1.1.1.1"),
            ("active_dns_ip", "1.1.1.1"),
            ("standby_domain_ip", "1.1.1.1"),
            ("standby_dns_ip", "1.1.1.1"),
            ("vpc", "vpc-name"),
            ("subnets", ["subnet-name-01", "subnet-name-02", ]),
            ("access_mode", "INTERNET"),
        ]
        parsed_args = self.check_parser(self.cmd, args, verify_args)

        # mock return values
        _network = base_resource.Resource(None, dict(id="network-id"))
        self.app.client_manager.network.find_network.return_value = _network
        _subnets = [base_resource.Resource(None, dict(id="subnet-id-1")),
                    base_resource.Resource(None, dict(id="subnet-id-2"))]
        self.app.client_manager.network.find_subnet.side_effect = _subnets
        _job = base_resource.DictWithMeta(dict(job_id="job_id"), 'RID')
        mocked_create.return_value = _job

        # take cmd
        result = self.cmd.take_action(parsed_args)

        json = {
            "ad_domains": {
                "domain_type": "LOCAL_AD",
                "domain_name": "test.com",
                "domain_admin_account": "test",
                "domain_password": "Test!@#$22",
                "active_domain_ip": "1.1.1.1",
                "active_dns_ip": "1.1.1.1",
                "standby_domain_ip": "1.1.1.1",
                "standby_dns_ip": "1.1.1.1",
            },
            "vpc_id": "network-id",
            "subnet_ids": [{
                "subnet_id": "subnet-id-1"
            }, {
                "subnet_id": "subnet-id-2"
            }],
            "access_mode": "INTERNET"
        }

        mocked_create.assert_called_once_with(
            "/workspaces", json=json, raw=True
        )
        self.assertEqual("Request Received, job id: %s" % _job["job_id"],
                         result)
