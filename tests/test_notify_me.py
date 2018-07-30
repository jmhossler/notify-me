from unittest.mock import patch

from notify_me.notify_me import notify_me


class TestNotifyMeSuite:
    requests.post.return_value == MagicMock(status_code=200)
    @patch('notify_me.notify_me.requests')
    def test_send_message(self, requests_mock):
        response = notify_me('message', {'url': '127.0.0.1'})

        requests_mock.post.assert_called_once_with('127.0.0.1', data={'message': 'message'})
        assert(response.status_code == 200)
