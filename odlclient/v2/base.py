import logging

from odlclient.openstack.common.apiclient.base import ManagerWithFind


LOG = logging.getLogger(__name__)


class Manager(ManagerWithFind):
    app = None
    has_container = False

    def _url(self, *args, **kw):
        parts = []
        if self.app is not None:
            parts.append(self.app)

        if self.has_container:
            container = kw.pop('container', None) or 'default'
            parts.append(container)

        parts.extend(args)
        url = "/".join([i for i in parts if i is not None])
        LOG.debug("Returning url %s", url)
        return url
