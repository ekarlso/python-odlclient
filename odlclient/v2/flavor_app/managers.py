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

from odlclient.v2.flavor_app.flavors import FlavorManager
from odlclient.v2.flavor_app.classes import ClassManager
from odlclient.v2.flavor_app.policy import PolicyManager

class FlavorAppManagers(object):
    def __init__(self, client):
        self.flavors = FlavorManager(client)
        self.classes = ClassManager(client)
        self.policy = PolicyManager(client)

