# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Dave Tucker <dave.j.tucker@hp.com>
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


class NeutronNetwork(base.Resource):
    pass

class NeutronPort(base.Resource):
    pass

class NeutronSubnet(base.Resource):
    pass

class NeutronBaseManager(Manager):
    """
    Base Class for Neutron Network/Subnet/Port Managers
    """
    base = 'controller/nb/v2/neutron'
    resource = None
    singular = None

    def list(self):
        """
        List Neutron Network/Subnet/Port
        """
        url = self._url(self.resource)
        return self._list(url, response_key=self.resource)

    def create(self, data):
        """
        Create a new Neutron Network/Subnet/Port

        :param data: JSON data
        """
        url = self._url(self.resource)
        self._post(url, data, response_key=self.singular)

    def get(self, uuid):
        """
        Get a Neutron Network/Subnet/Port

        :param net_uuid: UUID of the Network/Subnet/Port
        """
        url = self._url(self.resource, uuid)
        return self._get(url, response_key=self.singular)

    def update(self, uuid, data):
        """
        Update a Neutron Network/Subnet/Port

        :param net_uuid: UUID of the Network/Subnet/Port
        :param data: JSON Data
        """
        url = self._url(self.resource, uuid)
        return self._put(url, data, response_key=self.singular)

    def delete(self, uuid):
        """
        Delete a new Neutron Network/Subnet/Port

        :param net_uuid: UUID of the Network/Subnet/Port
        """
        url = self._url(self.resource, uuid)
        self._delete(url)

class NeutronNetworkManager(NeutronBaseManager):
    resource = 'networks'
    singular = 'network'
    resource_class = NeutronNetwork

class NeutronSubnetManager(NeutronBaseManager):
    resource = 'subnets'
    singular = 'subnet'
    resource_class = NeutronSubnet

class NeutronPortManager(NeutronBaseManager):
    resource = 'ports'
    singular = 'port'
    resource_class = NeutronPort

class NeutronManagers(object):
    def __init__(self, client):
        self.networks = NeutronNetworkManager(client)
        self.subnets = NeutronSubnetManager(client)
        self.ports = NeutronPortManager(client)
