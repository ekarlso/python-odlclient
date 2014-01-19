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
