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

#. desktop reboot(重启桌面)::

    $ openstack desktop reboot otcdemo03 --soft
    done

#. desktop start(启动桌面)::

    $ openstack desktop start otcdemo03
    done

#. desktop start(关闭桌面)::

    $ openstack desktop stop 393d8766-ee7b-48ee-9413-c818339a39ba
    done

#. --desktop delete(删除桌面)::

    $ openstack desktop delete 393d8766-ee7b-48ee-9413-c818339a39ba
    done

#. --desktop show(查看桌面详情)::

    $ openstack desktop show otcdemo03
    +-----------------+------------------------------------------------------------------------------------------------------------------+
    | Field           | Value                                                                                                            |
    +-----------------+------------------------------------------------------------------------------------------------------------------+
    | Desktop Id      | 393d8766-ee7b-48ee-9413-c818339a39ba                                                                             |
    | Computer Name   | otcdemo03                                                                                                        |
    | User Name       | otcdemo                                                                                                          |
    | Product Id      | workspace.g1.2xlarge.windows                                                                                     |
    | Security Groups | d3b0ce38-ef18-4997-9180-4f7eaa950ac7                                                                             |
    | Flavor          | g1.2xlarge                                                                                                       |
    | metadata        | charging_mode='0', image_name='Workspace_vGPU_User_Template1212',                                                |
    |                 | metering.cloudServiceType='sys.service.type.ec2', metering.image_id='5d760057-4b1c-4b0c-8a8e-8e3f60daba61',      |
    |                 | metering.imagetype='private', metering.resourcespeccode='g1.2xlarge.win', metering.resourcetype='1',             |
    |                 | os_bit='64', os_type='Windows', vpc_id='9b577224-d5dd-46b2-9a8c-ea8e850e912d'                                    |
    | addresses       | OS-EXT-IPS-MAC:mac_addr='fa:16:3e:be:e6:32', OS-EXT-IPS:type='fixed', addr='172.16.0.11', version='4'            |
    |                 | OS-EXT-IPS-MAC:mac_addr='fa:16:3e:be:e6:32', OS-EXT-IPS:type='floating', addr='100.64.233.20', version='4'       |
    | Root Volume     | size='80', type='SATA'                                                                                           |
    | Data Volumes    | size='80', type='SATA'                                                                                           |
    | Created         | 2016-12-28T09:32:21.000Z                                                                                         |
    | Login Status    | DISCONNECTED                                                                                                     |
    | Status          | ACTIVE                                                                                                           |
    +-----------------+------------------------------------------------------------------------------------------------------------------+
