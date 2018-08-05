from click.testing import CliRunner
from mock import patch

from notify_me.script import cli_script

class TestCliScriptSuite:
    @patch.dict('notify_me.script.os.environ', {'HOME': 'tests/data'})
    @patch('notify_me.script.notify_me')
    def test_simple_message(self, notify_me_mock):
        runner = CliRunner()
        result = runner.invoke(cli_script, ['message'])

        assert result.output == ''
        assert result.exit_code == 0
        notify_me_mock.assert_called_once_with(
                'message',
                {'url': '127.0.0.1'})

    @patch('notify_me.script.notify_me')
    def test_config_specification(self, notify_me_mock):
        runner = CliRunner()

        with runner.isolated_filesystem():
            with open('example.json', 'w') as f:
                f.write('{"url": "https://foo.bar:3512"}')

            result = runner.invoke(
                    cli_script,
                    ['message', '--config_file', 'example.json'])

            assert result.exit_code == 0
            assert result.output == ''
            notify_me_mock.assert_called_once_with(
                    'message',
                    {'url': 'https://foo.bar:3512'})
