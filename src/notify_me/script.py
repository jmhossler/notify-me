import click
import json
import os

from .notify_me import notify_me


@click.command()
@click.option('--config_file')
@click.argument('message')
def cli_script(message, config_file):
    if not config_file:
        notify_me(message, load(default_config_file()))
    else:
        notify_me(message, load(config_file))


def default_config_file():
    return os.getenv('HOME', '.') + '/.notify_me.json'


def load(config_file):
    with open(config_file) as f:
        return json.load(f)
