Commands
===============

1. desktop list(查询桌面列表)::

    $ openstack desktop list --user-name=otcdemo
        --os-workspace-endpoint-override=https://workspace.eu-de.otc.t-systems.com
    +--------------------------------------+---------------+-------------+--------------+--------------------------+
    | Desktop Id                           | Computer Name | User Name   | Ip Address   | Created                  |
    +--------------------------------------+---------------+-------------+--------------+--------------------------+
    | 393d8766-ee7b-48ee-9413-c818339a39ba | otcdemo03     | otcdemo     | 192.168.0.25 | 2016-12-28T09:32:21.000Z |
    | 2a010270-a011-415e-b1cd-3c484c8a8001 | otcdemo02     | otcdemo     | 192.168.0.24 | 2016-12-28T09:30:05.000Z |
    | 018b7f70-8d13-4e3c-a5d9-162ae6f34d8f | otcdemo01     | otcdemo     | 192.168.0.21 | 2016-12-24T08:58:59.000Z |
    +--------------------------------------+---------------+-------------+--------------+--------------------------+

2. desktop detail list(查询桌面详情列表)::

    $ openstack desktop detail list --user-name=otcdemo  --marker=393d8766-ee7b-48ee-9413-c818339a39ba
        --os-workspace-endpoint-override=https://workspace.eu-de.otc.t-systems.com
    +--------------------------------------+---------------+-----------+------------------------------+--------------+--------+
    | Desktop Id                           | Computer Name | User Name | Product Id                   | Login Status | Status |
    +--------------------------------------+---------------+-----------+------------------------------+--------------+--------+
    | 2a010270-a011-415e-b1cd-3c484c8a8001 | otcdemo02     | otcdemo   | workspace.c2.xlarge.windows  | DISCONNECTED | ACTIVE |
    | 018b7f70-8d13-4e3c-a5d9-162ae6f34d8f | otcdemo01     | otcdemo   | workspace.g1.2xlarge.windows | DISCONNECTED | ACTIVE |
    +--------------------------------------+---------------+-----------+------------------------------+--------------+--------+
