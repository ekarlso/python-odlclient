from odlclient.v2 import client as odlclient

http = odlclient.HTTPClient(
    'http://localhost:8080',
    username='admin',
    password='admin')

client = odlclient.Client(http)

node_type = 'OVS'
node_id = '10.10.0.24:54155'
table_name = 'open_vswitch'
row_uuid = '00bdb4f9-0d50-4793-bca3-f13c2e9d0eb5'

row = client.ovsdb.get(node_type, node_id, table_name, row_uuid)

print row
