import time
from deluge.log import LOG as log
from deluge.plugins.pluginbase import CorePluginBase
import deluge.component as component
import deluge.configmanager
from deluge.core.rpcserver import export
from twisted.internet import reactor
from twisted.internet.task import LoopingCall, deferLater

DEFAULT_PREFS = {
}

class Core(CorePluginBase):
    def enable(self):
        self.config = deluge.configmanager.ConfigManager("sequentialdownload.conf", DEFAULT_PREFS)
        # [("event_name", handler_function), ...]
        self.events = [("TorrentStateChangedEvent", state_changed_handler)]

        deferLater(reactor, 4, self.register)
        deferLater(reactor, 5, seq_all, True)

    def disable(self):
        deferLater(reactor, 0, self.deregister)
        deferLater(reactor, 1, seq_all, False)

    def update(self):
        pass

    @export
    def set_config(self, config):
        """Sets the config dictionary"""
        for key in config.keys():
            self.config[key] = config[key]
        self.config.save()

    @export
    def get_config(self):
        """Returns the config dictionary"""
        return self.config.config

    def register(self):
        em = component.get("EventManager")
        for arg in self.events:
            em.register_event_handler(*arg)

    def deregister(self):
        em = component.get("EventManager")
        for arg in self.events:
            em.deregister_event_handler(*arg)

def state_changed_handler(tid, *arg):
    state = arg[0]
    if state == 'Downloading':
        tor = component.get("TorrentManager").torrents[tid]
        set_seq_t1(tor, True)

def set_seq_t1(tor, flag):
    info = tor.torrent_info
    handle = tor.handle
    if info and handle:
        log.info("Setting sequential_download:%s for %s", flag, info.name())
        handle.set_sequential_download(flag)
    else:
        deferLater(reactor, 3, set_seq_t1, tor, flag)

def seq_all(flag):
    for tor in component.get("TorrentManager").torrents.values():
        set_seq_t1(tor, flag)
