import notify_me


@notify_me.hookimpl(specname="notify_me")
def hello_notification(config):
    print("Hello, world")
