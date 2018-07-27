from unittest.mock import patch

from notify_me.script import notify_me


class TestNotifyMeSuite:
    @patch('notify_me.script.requests')
    def test_send_message(self, requests_mock):
        response = notify_me('message', {'url': '127.0.0.1'})

        requests_mock.post.assert_called_once_with('127.0.0.1', data={'message': 'message'})
        assert(response.status_code == 200)