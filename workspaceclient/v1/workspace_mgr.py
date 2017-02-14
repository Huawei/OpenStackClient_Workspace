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


class WorkspaceManager(manager.Manager):
    """Workspace workspace API management"""

    resource_class = resource.Workspace

    def create(self):
        """create a new workspace"""
        {
            "ad_domains": {
                "domain_type": "LITE_AD",
                "domain_name": "testapi.litead.com",
                "domain_admin_account": "vdsadmin",
                "domain_password": "Testabc!23"
            },
            "vpc_id": "e8f985fa-5161-4cb8-bf5a-155058ea58c9",
            "subnet_ids": [
                {
                    "subnet_id": "067b30a9-1b73-4804-a808-699c5f6c4e09"
                },
                {
                    "subnet_id": "47c39964-4a32-4fb9-acc8-fac4355848d0"
                }
            ],
            "access_mode": "INTERNET"
        }
        self._create("/workspaces")

    def edit(self):
        self._update_all("/workspaces")

    def get(self):
        """get workspace detail"""
        return self._get("/workspaces")

    def delete(self):
        """delete workspace

        this is a asynchronous task
        """
        return self._delete("/workspaces")
