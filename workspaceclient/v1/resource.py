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
from workspaceclient.common import display
from workspaceclient.common import resource


class Desktop(resource.Resource, display.Display):
    """workspace desktop resource instance"""

    show_column_names = [

    ]

    list_column_names = [
        "Desktop Id",
        "Computer Name",
        "User Name",
        "Ip Address",
        "Created"
    ]

    list_detail_column_names = [
        "Desktop Id",
        "Computer Name",
        "User Name",
        "Product Id",
        "Login Status",
        "Status"
    ]
