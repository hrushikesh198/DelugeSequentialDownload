from deluge.log import LOG as log
from deluge.ui.client import client
from deluge import component
from deluge.plugins.pluginbase import WebPluginBase

from common import get_resource


class WebUI(WebPluginBase):
    scripts = [get_resource("sequentialdownload.js")]

    def enable(self):
        pass

    def disable(self):
        pass
