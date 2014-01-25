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
from odlclient.v2.base import Manager

class OvsdbManager(Manager):
    base = 'ovsdb/nb/v2'

    def list(self, node_type, node_id, table_name):
        url = self._url('node', node_type, node_id ,
                        'tables', table_name, 'rows')
        return self._list(url)

    def create(self, node_type, node_id, table_name, data):
        url = self._url('node', node_type, node_id ,
                        'tables', table_name, 'rows')
        return self._post(url, data, return_raw=True)

    def get(self, node_type, node_id, table_name, row_uuid):
        url = self._url('node', node_type, node_id ,
                        'tables', table_name, 'rows', row_uuid)
        return self._get(url, return_raw=True)

    def delete(self, node_type, node_id, table_name, row_uuid):
        url = self._url('node', node_type, node_id ,
                        'tables', table_name, 'rows', row_uuid)
        return self._delete(url)

    def update(self, node_type, node_id, table_name, row_uuid):
        url = self._url('node', node_type, node_id ,
                        'tables', table_name, 'rows', row_uuid)
        return self._put(url, return_raw=True)



