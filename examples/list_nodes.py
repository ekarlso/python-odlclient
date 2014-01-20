from odlclient.v2 import client as odlclient


http = odlclient.HTTPClient(
    'http://localhost:8080/controller/nb/v2',
    username='admin',
    password='admin')

client = odlclient.Client(http)

client.nodes.list()
