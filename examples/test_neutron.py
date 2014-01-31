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

print networks
print ports
print subnets
