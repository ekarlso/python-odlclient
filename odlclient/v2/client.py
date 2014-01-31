# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Endre Karlson <endre.karlson@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import logging
import requests

from odlclient.openstack.common.apiclient import client
from odlclient.v2.bridge_domain import BridgeDomain
from odlclient.v2.connection_manager import ConnectionManager
from odlclient.v2.node import NodeManager
from odlclient.v2.ovsdb import OvsdbManager
from odlclient.v2.subnet import SubnetManager
from odlclient.v2.staticroute import StaticRouteManager
from odlclient.v2.neutron import NeutronManagers


LOG = logging.getLogger(__name__)


class HTTPClient(client.HTTPClient):
    """
    Modified HTTPClient to take a endpoint and doesn't use X-Auth-Token
    """
    user_agent = "odlclient.openstack.common.apiclient"

    def __init__(self,
                 endpoint,
                 username=None,
                 password=None,
                 original_ip=None,
                 verify=True,
                 cert=None,
                 timeout=None,
                 timings=False,
                 keyring_saver=None,
                 debug=False,
                 user_agent=None,
                 http=None):

        self.endpoint = endpoint
        self.username = username
        self.password = password

        self.original_ip = original_ip
        self.timeout = timeout
        self.verify = verify
        self.cert = cert

        self.keyring_saver = keyring_saver
        self.debug = debug
        self.user_agent = user_agent or self.user_agent

        self.times = []  # [("item", starttime, endtime), ...]
        self.timings = timings

        # requests within the same session can reuse TCP connections from pool
        self.http = http or requests.Session()

        if self.username and self.password:
            self.http.auth = (self.username, self.password)

    def client_request(self, client, method, url, **kwargs):
        try:
            return self.request(
                method, self.concat_url(self.endpoint, url), **kwargs)
        except Exception as e:
            if hasattr(e, 'details'):
                LOG.error("Error from server below:\n%s", e.details)
            raise


class Client(client.BaseClient):
    def __init__(self, *args, **kw):
        super(Client, self).__init__(*args, **kw)
        self.bridge_domain = BridgeDomain(self)
        self.connection_manager = ConnectionManager(self)
        self.nodes = NodeManager(self)
        self.ovsdb = OvsdbManager(self)
        self.subnets = SubnetManager(self)
        self.staticroutes = StaticRouteManager(self)
        self.neutron = NeutronManagers(self)
