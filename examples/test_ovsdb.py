import logging
import pprint

from odlclient.v2 import client as odlclient

logging.basicConfig(level='DEBUG')

http = odlclient.HTTPClient(
    'http://localhost:8080',
    username='admin',
    password='admin')

client = odlclient.Client(http)

connections = client.connection_manager.list()
for n in connections:
    if n.type == 'OVS':
        print "Getting OVSDB bridges"
        rows = client.ovsdb.list(n.type, n.id, 'open_vswitch')
        for r in rows.values():
            pprint.pprint(r)
