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


class BridgeDomain(base.Resource):
    @property
    def id(self):
        return self.name


class BridgeDomain(Manager):
    app = 'bridgedomain'

    def list(self):
        """
        List BridgeDomains.
        """
        url = self._url('nodes')
        return self._list(url)

    def create(self, node_type, node_id):
        """
        Create a new BridgeDomain.

        :param node_type: Node Type.
        :param node_id: Node ID.
        """
        url = self._url('node', node_type, node_id)
        self._post(url)

    def delete(self, node_type, node_id):
        """
        Delete a new BridgeDomain.

        :param node_type: Node Type.
        :param node_id: Node ID.
        """
        url = self._url('node', node_type, node_id)
        self._delete(url)

    def create_port(self, node_type, node_id, name, vlan=None):
        """
        Create a Port in a BridgeDomain.

        :param node_type: Node Type.
        :param node_id: Node ID.
        :param name: Name of the Port.
        :param vlan: Optional VLAN.
        """

        url = self._url('node', node_type, node_id, name, vlan)
        self._post(url)

    def delete_port(self, node_type, node_id, name):
        """
        Delete a Port in a BridgeDomain.

        :param node_type: Node Type.
        :param node_id: Node ID.
        :param name: Name of the Port
        """
        url = self._url('node', node_type, node_id, name)
        self._delete(url)
