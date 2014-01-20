from odlclient.openstack.common.apiclient import base
from odlclient.v2.base import Manager


class Connection(base.Resource):
    pass


class ConnectionManager(Manager):
    app = 'connectionmanager'
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
