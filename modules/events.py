import discord
import traceback
import sys
from discord.ext import commands


class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("Ready!")

    async def on_message(self, message):
        if message.author.bot:
            return

    async def on_command_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, discord.Forbidden):
            return
        elif isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.NotOwner):
            return await ctx.send("You're not the owner of this bot.")
        print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr
        )


def setup(bot):
    bot.add_cog(Events(bot))
