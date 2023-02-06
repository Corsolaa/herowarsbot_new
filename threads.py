channel = bot.get_channel(...) # define this!
await channel.create_thread(name="Thread Name", message=None, auto_archive_duration=60, type=None, reason=None)
