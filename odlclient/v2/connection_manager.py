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
from odlclient.openstack.common.apiclient import base
from odlclient.v2.base import Manager


class Connection(base.Resource):
    pass


class ConnectionManager(Manager):
    base = 'controller/nb/v2/connectionmanager'
    resource_class = Connection

    def list(self):
        """
        List Connections
        """
        url = self._url('nodes')
        return self._list(url, response_key='node')

    def create(self, node_id, ip_address, port, node_type=None):
        """
        Create / Set a management connection to a Node.

        :param node_id: Node ID
        :param ip_address: IP Address for the Connection.
        :param port: Port for the Connection.
        :param node_type: Optional, if known the Node type like OF.
        """
        parts = ['node', node_id, 'address', ip_address, 'port', port]
        if node_type:
            parts.insert(1, node_type)
        url = self._url(*parts)

        return self._put(url)

    def delete(self, node_type, node_id):
        """
        Delete / Unset a Connection to a Node.
        """
        url = self._url('node', node_type, node_id)
        self._delete(url)
