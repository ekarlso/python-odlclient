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


class StaticRoute(base.Resource):
    @property
    def id(self):
        return self.name


class StaticRouteManager(Manager):
    base = 'controller/nb/v2/staticroute'
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
