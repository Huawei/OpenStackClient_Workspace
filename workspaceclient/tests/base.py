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
from workspaceclient.tests import fakes
from workspaceclient.v1 import antiddos_mgr
from mock import mock
from osc_lib.tests import utils


class BaseTestCase(utils.TestCommand):
    """Base Test case class for all unit tests."""
    pass


class AntiDDosV1BaseTestCase(BaseTestCase):
    """Base test case class for AntiDDos V1 management API."""

    def __init__(self, *args, **kwargs):
        super(AntiDDosV1BaseTestCase, self).__init__(*args, **kwargs)
        self.cmd = None
        self._antiddos = None
        self.mocked_find = None

    def setUp(self):
        super(AntiDDosV1BaseTestCase, self).setUp()
        fake_antiddos_client = fakes.FakeAntiDDosV1Client()
        self.app.client_manager.antiddos = fake_antiddos_client
