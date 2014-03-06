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
import logging

logging.basicConfig(level='DEBUG')

from odlclient.v2 import client as odlclient

http = odlclient.HTTPClient(
    'http://10.10.0.20:8080',
    username='admin',
    password='admin')

client = odlclient.Client(http)

networks = client.neutron.networks.list()
ports = client.neutron.ports.list()
subnets = client.neutron.subnets.list()

print(networks)
print(ports)
print(subnets)
