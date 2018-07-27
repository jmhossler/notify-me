import requests


def notify_me(message, config):
    return requests.post(config['url'], data={'message': message})