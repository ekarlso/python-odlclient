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

class FwdClass(base.Resource):
    @property
    def id(self):
        return self.id

class ClassManager(Manager):
    base = 'controller/nb/v2/policy/default'
    resource_class = FwdClass

    def list(self, container=None):
        """
        List Classes

        :param container: Container if any.
        """
        url = self._url('fwdClasses', container=container)
        classes = self._list(url, 'fwdClassList')
        return classes

    def get(self, id, container=None):
        """
        Get a Class

        :param id: Id to get
        :param container: Container if any.
        """
        url = self._url('fwdClass', id, container=container)
        return self._get(url)

    def create(self, name, application_property,
               application_policy, container=None):
        """
        Create a FwdClass

        :param name: The name of the Flavor
        :param application_property: Applciation Property
        :param application_policy: Application_Policy
        """
        url = self._url('fwdClass', container=container)

        json = {
            "name": name,
            "application_property": application_property,
            "application_policy": application_policy
        }

        self._post(url, json=json, return_raw=True)

    def delete(self, id, container=None):
        """
        Delete a StaticRoute.

        :param id: Flavor ID to delete
        :param container: Container if any.
        """
        url = self._url('fwdClass', id, container=container)
        self._delete(url)
