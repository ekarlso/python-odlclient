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
        print connector
