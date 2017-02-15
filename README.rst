python-workspaceclient
======================

This is a `OpenStack Client`_ plugin for HuaWei Workspace Management API which
provides **command-line scripts** (integrated with openstack) and Python library for
accessing the Workspace management API.


Installation
------------
Currently, We can install the plugin from source code

.. code:: console

    $ git clone https://github.com/Huawei/OpenStackClient_Workspace
    python-workspaceclient
    $ cd python-workspaceclient
    # use python setup.py develop for test purpose
    $ python setup.py install
    $ pip install -r requirements.txt

Command Line Client Usage
-------------------------
::

    This plugin is integrated with `OpenStack Client`_ , so the command line
    client has all features openstack provided.

User help command::

    $ openstack --help
    usage: openstack [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
                 [--os-cloud <cloud-config-name>]
                 [--os-region-name <auth-region-name>]
                 [--os-cacert <ca-bundle-file>] [--os-cert <certificate-file>]
                 [--os-key <key-file>] [--verify | --insecure]
                 [--os-default-domain <auth-domain>]
                 [--os-interface <interface>] [--timing] [--os-beta-command]
                 [--os-profile hmac-key]
                 [--os-compute-api-version <compute-api-version>]
                 [--os-network-api-version <network-api-version>]
                 [--os-image-api-version <image-api-version>]
                 [--os-volume-api-version <volume-api-version>]
                 [--os-identity-api-version <identity-api-version>]
                 [--os-object-api-version <object-api-version>]
                 [--os-queues-api-version <queues-api-version>]
                 [--os-clustering-api-version <clustering-api-version>]
                 [--os-search-api-version <search-api-version>]
                 .......



Provided Commands

*The command line client is self-documenting. Use the --help or -h flag to
access the usage options. You can find more command line client examples* `here <./commands.rst>`_


+------------------------+
| desktop list           |
+------------------------+
| desktop detail list    |
+------------------------+
| desktop create         |
+------------------------+
| desktop delete         |
+------------------------+
| desktop reboot         |
+------------------------+
| desktop start          |
+------------------------+
| desktop stop           |
+------------------------+
| desktop edit           |
+------------------------+
| desktop show           |
+------------------------+
| desktop user list      |
+------------------------+
| desktop login list     |
+------------------------+
| workspace enable       |
+------------------------+
| workspace show         |
+------------------------+
| workspace edit         |
+------------------------+
| workspace disable      |
+------------------------+
| workspace policy show  |
+------------------------+
| workspace policy edit  |
+------------------------+
| workspace product list |
+------------------------+


Python Library Usage
-------------------------------

The full api is documented in the `Workspace Offical Document`_ site

Here's an example of listing metric types using Python library with keystone V3 authentication:

.. code:: python

    >>> from keystoneauth1 import session
    >>> from keystoneauth1 import client
    >>> from cloudeyeclient.v1 import client

    >>> # Use Keystone API v3 for authentication as example
    >>> auth = identity.v3.Password(auth_url=u'http://localhost:5000/v3',
    ...                             username=u'admin_user',
    ...                             user_domain_name=u'Default',
    ...                             password=u'password',
    ...                             project_name=u'demo',
    ...                             project_domain_name=u'Default')

    >>> # Next create a Keystone session using the auth plugin we just created
    >>> session = session.Session(auth=auth)

    >>> # Now we use the session to create a CloudEye client
    >>> client = client.Client(session=session)

    >>> # Then we can access all Workspace API
    >>> # Let's try get workspace API
    >>> client.workspaces.get()
    <Metric domain_type=LITE_AD ....>


.. note::

    The example above must be running and configured to use the Keystone Middleware.

    For more information on setting this up please visit: `KeyStone`_


* License: Apache License, Version 2.0
* `OpenStack Client`_
* `Workspace Offical Document`_
* `KeyStone`_

.. _OpenStack Client: https://github.com/openstack/python-openstackclient
.. _Workspace Offical Document: http://support.hwclouds.com/workspace/index.html
.. _KeyStone: http://docs.openstack.org/developer/keystoneauth/
