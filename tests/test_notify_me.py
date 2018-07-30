from unittest.mock import patch

from notify_me.notify_me import notify_me


class TestNotifyMeSuite:
    @patch('notify_me.notify_me.requests')
    def test_send_message(self, requests_mock):
        response = notify_me('message', {'url': '127.0.0.1'})

<<<<<<< HEAD
        requests_mock.post.assert_called_once_with('127.0.0.1', data={'message': 'message'})
        assert(response.status_code == 200)
=======
        requests_mock.post.assert_called_once_with('127.0.0.1', json={'message': 'message'})
>>>>>>> c6d50b0c8265f2a4da1faf6f0c756582d40af882
