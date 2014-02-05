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
from datetime import datetime
import time

from odlclient.openstack.common.apiclient import base
from odlclient.v2.base import Manager


class Node(base.Resource):
    @property
    def id(self):
        return self.node['id']

    @property
    def type(self):
        return self.node['type']

    @property
    def description(self):
        data = self._info['properties']['description']['value']
        return None if data == 'None' else data

    @property
    def connected_since(self):
        data = self._info['properties']['timeStamp']['value']
        return datetime.fromtimestamp(time.mktime(time.gmtime(data / 1000)))


class NodeConnector(base.Resource):
    pass


class NodeManager(Manager):
    base = 'controller/nb/v2/switchmanager'
    has_container = True
    resource_class = Node

    def list(self, container=None):
        url = self._url('nodes', container=container)
        return self._list(url, response_key='nodeProperties')

    def save(self, container=None):
        url = self._url('nodes', container=container)
        self._post(url)

    def list_connectors(self, node_type, node_id, container=None):
        url = self._url('node', node_type, node_id, container=container)
        return self._list(url, response_key='nodeConnectorProperties',
                          obj_class=NodeConnector)

    def create_property(self, node_type, node_id, name, value, container=None):
        url = self._url(
            'node', node_type, node_id, 'property', name, value,
            container=container)
        self._put(url, value)

    def delete_property(self, node_type, node_id, name, value, container=None):
        url = self._url(
            'node', node_type, node_id, 'property', name, value,
            container=container)
        self._delete(url)

    def create_connector_property(self, node_type, node_id, connector_type,
                                  connector_name, name, value, container=None):
        url = self._url('nodeconnector', node_type, node_id, connector_name,
                        'property', name, value, container=container)
        self._put(url, value)

    def delete_connector_property(self, node_type, node_id, connector_type,
                                  connector_name, name, value, container=None):
        url = self._url('nodeconnector', node_type, node_id, connector_name,
                        'property', name, value, container=container)
        self._delete(url, value)
