from odlclient.openstack.common.apiclient import base
from odlclient.v2.base import Manager


class Node(base.Resource):
    @property
    def id(self):
        return self.node['id']

    @property
    def type(self):
        return self.node['type']


class NodeManager(Manager):
    app = 'switchmanager'
    has_container = True
    resource_class = Node

    def list(self, container=None):
        url = self._url('nodes', container=container)
        return self._list(url, response_key='nodeProperties')

    def save(self, container=None):
        url = self._url('nodes', container=container)
        self._post(url)

    def get(self, node_type, node_id, container=None):
        url = self._url(node_type, node_id, container=container)
        return self._get(url)

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
