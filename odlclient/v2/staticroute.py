from odlclient.openstack.common.apiclient import base
from odlclient.v2.base import Manager


class StaticRoute(base.Resource):
    @property
    def id(self):
        return self.name


class StaticRouteManager(Manager):
    app = 'staticroute'
    has_container = True
    resource_class = StaticRoute

    def list(self, container=None):
        """
        List StaticRoutes.

        :param container: Container if any.
        """
        url = self._url('routes', container=container)
        staticroutes = self._list(url, 'staticRoute')
        return staticroutes

    def get(self, name, container=None):
        """
        Get a StaticRoute

        :param name: Name to get
        :param container: Container if any.
        """
        url = self._url('route', name, container=container)
        return self._get(url)

    def create(self, name, prefix, nexthop, container=None):
        """
        Create a StaticRoute.

        :param name: The name of the StaticRoute
        :param prefix: IPvX prefix.
        :param nexthop: Nexthop for the StaticRoute
        """
        url = self._url('route', name, container=container)

        json = {
            "name": name,
            "prefix": prefix,
            "nextHop": nexthop
        }

        self._put(url, json=json)

    def delete(self, name, container=None):
        """
        Delete a StaticRoute.

        :param name: Name to delete
        :param container: Container if any.
        """
        url = self._url('route', name, container=container)
        self._delete(url)
