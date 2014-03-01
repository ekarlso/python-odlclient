import logging
import pprint

from odlclient.v2 import client as odlclient

logging.basicConfig(level='DEBUG')

http = odlclient.HTTPClient(
    'http://madhu.ngrok.com',
    username='admin',
    password='admin')

client = odlclient.Client(http)

# Test Get operations
print client.flavor_app.flavors.list()
print client.flavor_app.classes.list()
print client.flavor_app.policy.list()

# Test Post operations
class_id = client.flavor_app.classes.create("test", "Number",
                                            "Hop Count based Shortest Path")

flavor_id = client.flavor_app.flavors.create("test", "Dave's Test Flavor",
                                             class_id)

policy_id = client.flavor_app.policy.create("testuuid123456", flavor_id)


