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
    'http://localhost:8080',
    username='admin',
    password='admin')

client = odlclient.Client(http)

nodes = client.nodes.list()

if nodes:
    node = nodes[0]
    connectors = client.nodes.list_connectors(node.type, node.id)

    for connector in connectors:
        print(connector)
