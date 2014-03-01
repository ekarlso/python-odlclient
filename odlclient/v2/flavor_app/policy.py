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

class Policy(base.Resource):
    @property
    def id(self):
        return self.id

class PolicyManager(Manager):
    base = 'ovsdb/nb/v2/neutron'
    resource_class = Policy

    def list(self, container=None):
        """
        List Policy

        :param container: Container if any.
        """
        url = self._url('tenantFlavors', container=container)
        policies = self._list(url, 'tenantMaps')
        return policies

    def get(self, id, container=None):
        """
        Get a Policy

        :param id: Id to get
        :param container: Container if any.
        """
        url = self._url('tenantFlavor', id, container=container)
        return self._get(url)

    def create(self, tenant_uuid, flavor, container=None):
        """
        Create a Policy element

        :param tenant_uuid: Tenant UUID
        :param flavor: Flavor ID
        """
        url = self._url('tenantFlavor', container=container)

        json = {
            "tenant_uuid": tenant_uuid,
            "flavor": flavor
        }

        self._post(url, json=json, return_raw=True)

    def delete(self, id, container=None):
        """
        Delete a Policy element

        :param id: Policy element ID to delete
        :param container: Container if any.
        """
        url = self._url('tenantFlavor', id, container=container)
        self._delete(url)


