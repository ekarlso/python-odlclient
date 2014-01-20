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


class Subnet(base.Resource):
    @property
    def id(self):
        return self.name
    pass


class SubnetManager(Manager):
    app = 'subnetservice'
    has_container = True
    resource_class = Subnet

    def list(self, container=None):
        """
        List Subnets.

        :param container: Container if any.
        """
        url = self._url('subnets', container=container)
        staticsubnets = self._list(url, 'subnetConfig')
        return staticsubnets

    def get(self, name, container=None):
        """
        :param name: Name to get
        :param container: Container if any.
        """
        url = self._url('subnet', name, container=container)
        return self._get(url)

    def create(self, name, subnet, connectors=[], container=None):
        """
        Create a new Subnet.

        :param name: The name of the Subnet
        :param subnet: IPvX subnet: 10.0.0.0/24.
        :param connectors: List of connectors.
        :param container: Container if any.
        """
        url = self._url('subnet', name, container=container)

        json = {
            "name": name,
            "subnet": subnet,
            "nodeConnectors": connectors
        }

        self._put(url, json=json)

    def delete(self, name, container=None):
        """
        Delete a Subnet.

        :param name: Name to delete
        :param container: Container if any.
        """
        url = self._url('subnet', name, container=container)
        self._delete(url)

    def update_ports(self, name, connectors=[], container=None):
        """
        Set the Node connectors of the Subnet.

        :param name: The name of the Subnet
        :param connectors: List of connectors.
        """
        url = self._url('subnet', name, container=container)
        json = {
            'nodeConnectors': connectors
        }
        self._post(url, json)
