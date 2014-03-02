import logging
import pprint

from odlclient.v2 import client as odlclient

logging.basicConfig(level='DEBUG')

http = odlclient.HTTPClient(
    'http://madhu.ngrok.com',
    username='admin',
    password='admin')

client = odlclient.Client(http)

# Test List operations
print client.flavor_app.flavors.list()
print client.flavor_app.classes.list()
print client.flavor_app.policy.list()

# Test Create operations
class_id = client.flavor_app.classes.create("test", "Number",
                                            "Hop Count based Shortest Path")
flavor_id = client.flavor_app.flavors.create("test", "Dave's Test Flavor",
                                             class_id)
policy_id = client.flavor_app.policy.create("testuuid123456", flavor_id)

# Test Delete Operations
client.flavor_app.policy.delete(policy_id)
client.flavor_app.flavors.delete(flavor_id)
client.flavor_app.classes.delete(class_id)

for policy in client.flavor_app.policy.list():
    assert flavor_id != policy.id

for flavors in client.flavor_app.flavors.list():
    assert flavor_id != flavors.id

for classes in client.flavor_app.classes.list():
    assert class_id != classes.id

