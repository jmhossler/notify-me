import getpass
import notify_me


@notify_me.hookimpl(specname="notify_me")
def basic_notification():
    """This is a basic implemetnation of a notification plugin! It also acts as
    notify-me's most simple plugin, with just simple output to stdout actingn
    as the notification
    """
    print(f"All notifications sent, {getpass.getuser()}")
