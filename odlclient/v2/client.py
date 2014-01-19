import requests

from odlclient.openstack.common.apiclient import client
from odlclient.v2.bridge_domain import BridgeDomain
from odlclient.v2.connection_manager import ConnectionManager
from odlclient.v2.subnet import SubnetManager
from odlclient.v2.staticroute import StaticRouteManager


class HTTPClient(client.HTTPClient):
    """
    Modified HTTPClient to take a endpoint and doesn't use X-Auth-Token
    """
    user_agent = "odlclient.openstack.common.apiclient"

    def __init__(self,
                 endpoint,
                 username=None,
                 password=None,
                 original_ip=None,
                 verify=True,
                 cert=None,
                 timeout=None,
                 timings=False,
                 keyring_saver=None,
                 debug=False,
                 user_agent=None,
                 http=None):

        self.endpoint = endpoint
        self.username = username
        self.password = password

        self.original_ip = original_ip
        self.timeout = timeout
        self.verify = verify
        self.cert = cert

        self.keyring_saver = keyring_saver
        self.debug = debug
        self.user_agent = user_agent or self.user_agent

        self.times = []  # [("item", starttime, endtime), ...]
        self.timings = timings

        # requests within the same session can reuse TCP connections from pool
        self.http = http or requests.Session()

        if self.username and self.password:
            self.http.auth = (self.username, self.password)

    def client_request(self, client, method, url, **kwargs):
            return self.request(
                method, self.concat_url(self.endpoint, url), **kwargs)


class Client(client.BaseClient):
    def __init__(self, *args, **kw):
        super(Client, self).__init__(*args, **kw)
        self.bridge_domain = BridgeDomain(self)
        self.connection_manager = ConnectionManager(self)
        self.subnets = SubnetManager(self)
        self.staticroutes = StaticRouteManager(self)
