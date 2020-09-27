==========
Notify Me!
==========

I created this tool originally so I can do some action when a long-running
command is over. This is mainly centered around long builds. I won't spend to
much time arguing for why I built this tool, so far I'm only building this for
me. If you think you'd find this useful with some extra functionality, feel
free to put up an issue. It is very barebones at the moment.

Creating a Plugin
=================

I used pluggy as a plugin manager, and you can see an example of a plugin in
notify_me/lib.py. The important part for your plugin entrypoint is a specific
decorator, and to know the specification name.

The hook specification is under notify_me/hookspecs.py. You can have fewer
arguments, but for now the only argument passed down is config. I'll go more
into that later, though that is pretty simple.

To specify what function is the hook for your plugin, you use this decorator:

.. code-block:: python

  @notify_me.hookimpl

The example, basic notification, looks like this:

.. code-block:: python

  import getpass
  import notify_me


  @notify_me.hookimpl(specname="notify")
  def basic_notification():
      """This is a basic implemetnation of a notification plugin! It also acts as
      notify-me's most simple plugin, with just simple output to stdout actingn
      as the notification
      """
      print(f"All notifications sent, {getpass.getuser()}")

A quirk is that the, unless `specname="notify"` is used, the function name needs
to be `notify`

Configuration
=============

Config location: `~/.config/notify_me/config.ini`

I used the configurationparser package, so if you add configuration to that file,
you should have access to it from your plugin. I did this so we could keep
secrets outside of our plugins, but obviously it can be used to make you're
plugin more generic.
