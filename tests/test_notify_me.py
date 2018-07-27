from unittest.mock import patch

from notify_me.notify_me import notify_me


class TestNotifyMeSuite:
    @patch('notify_me.notify_me.requests')
    def test_send_message(self, requests_mock):
        notify_me('message', {'url': '127.0.0.1'})

        requests_mock.post.assert_called_once_with('127.0.0.1', json={'message': 'message'})
