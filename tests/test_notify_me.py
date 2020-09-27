import os
import pytest

from unittest.mock import MagicMock
from notify_me import host, hookimpl


@pytest.fixture
def plugin_manager():
    return host.get_plugin_manager()


@pytest.fixture
def notify_me_plugin_impl(plugin_manager):
    mock_notify_me_impl = MagicMock()

    class TestPlugin:
        @hookimpl
        def notify_me(self, config):
            mock_notify_me_impl(config)

    plugin_manager.register(TestPlugin())
    return mock_notify_me_impl


def test_notify_me_calls_plugins_with_config(notify_me_plugin_impl, mocker):
    # Replace configuration file path with test configuration file
    mock_configuration = MagicMock()
    mocker.patch("notify_me.host.get_configuration", return_value=mock_configuration)

    host.main()

    notify_me_plugin_impl.assert_called_once_with(mock_configuration)


def test_notify_me_will_not_load_invalid_plugins(plugin_manager):
    mock_invalid_notify_me_impl = MagicMock()

    class BadPlugin:
        @hookimpl
        def do_something_else(self, config):
            mock_invalid_notify_me_impl(config)

    plugin_manager.register(BadPlugin())

    host.main()

    mock_invalid_notify_me_impl.assert_not_called()
