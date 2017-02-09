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
from osc_lib import utils
from workspaceclient.common import display
from workspaceclient.common import resource


class Desktop(resource.Resource, display.Display):
    """workspace desktop resource instance"""

    {
        "security_groups": [
            {
                "id": "d3b0ce38-ef18-4997-9180-4f7eaa950ac7"
            }
        ],
        "flavor": {
            "id": "g1.2xlarge",
            "links": [
                {
                    "rel": "bookmark",
                    "hrel": "https://compute.region.eu-de.otc-tsi.de/075c841533dd4d7396a133b435a9e51c/flavors/g1.2xlarge"
                }
            ]
        },
        "metadata": {
            "metering.image_id": "5d760057-4b1c-4b0c-8a8e-8e3f60daba61",
            "metering.imagetype": "private",
            "metering.resourcespeccode": "g1.2xlarge.win",
            "metering.cloudServiceType": "sys.service.type.ec2",
            "image_name": "Workspace_vGPU_User_Template1212",
            "metering.resourcetype": "1",
            "os_bit": "64",
            "vpc_id": "9b577224-d5dd-46b2-9a8c-ea8e850e912d",
            "os_type": "Windows",
            "charging_mode": "0"
        },
        "addresses": {
            "9b577224-d5dd-46b2-9a8c-ea8e850e912d": [
                {
                    "addr": "172.16.0.9",
                    "version": 4,
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:8c:cf:63",
                    "OS-EXT-IPS:type": "fixed"
                },
                {
                    "addr": "100.64.226.125",
                    "version": 4,
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:8c:cf:63",
                    "OS-EXT-IPS:type": "floating"
                }
            ],
            "62615060-5a38-42d4-a391-9b8a109da548": [
                {
                    "addr": "192.168.0.21",
                    "version": 4,
                    "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:d8:03:c6",
                    "OS-EXT-IPS:type": "fixed"
                }
            ]
        },
        "product_id": "workspace.g1.2xlarge.windows",
        "root_volume": {
            "type": "SATA",
            "size": 80
        },
        "data_volumes": []
    }

    show_column_names = [
        "Desktop Id",
        "Computer Name",
        "User Name",
        "Product Id",
        "Security Groups",
        "Created",
        "Login Status",
        "Status"
    ]

    formatter = {
        "Security Groups": utils.format_list
    }

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
