import configparser
import os
import pluggy

from notify_me import hookspecs
from singleton_decorator import singleton


def main():
    config = get_configuration()
    plugin_manager = get_plugin_manager()
    plugin_manager.load_setuptools_entrypoints("notify")

    plugin_manager.hook.notify_me(config=config)


def get_configuration():
    config = configparser.ConfigParser()
    config.read(get_configuration_file())
    return config


def get_plugin_manager():
    return NotifyMePluginManager().plugin_manager


def get_configuration_file():
    return os.path.expanduser("~/.config/notify_me/config.ini")


@singleton
class NotifyMePluginManager:
    def __init__(self):
        self.plugin_manager = pluggy.PluginManager("notify_me")
        self.plugin_manager.add_hookspecs(hookspecs)
