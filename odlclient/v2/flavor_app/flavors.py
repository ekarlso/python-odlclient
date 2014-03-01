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

class Flavor(base.Resource):
    @property
    def id(self):
        return self.id

class FlavorManager(Manager):
    base = 'controller/nb/v2/policy/default'
    resource_class = Flavor

    def list(self, container=None):
        """
        List Flavors

        :param container: Container if any.
        """
        url = self._url('flavors', container=container)
        flavors = self._list(url, 'flavorList')
        return flavors

    def get(self, id, container=None):
        """
        Get a Flavor

        :param id: Id to get
        :param container: Container if any.
        """
        url = self._url('flavor', id, container=container)
        return self._get(url)

    def create(self, name, description, fwd_class, container=None):
        """
        Create a Flavor

        :param name: The name of the Flavor
        :param description: Description
        :param fwd_class: Forwarding class for the flavor
        """
        url = self._url('flavor', container=container)

        json = {
            "name": name,
            "description": description,
            "fwd_class": fwd_class
        }

        self._post(url, json=json, return_raw=True)

    def delete(self, id, container=None):
        """
        Delete a StaticRoute.

        :param id: Flavor ID to delete
        :param container: Container if any.
        """
        url = self._url('flavor', id, container=container)
        self._delete(url)
