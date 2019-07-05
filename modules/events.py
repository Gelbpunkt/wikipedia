import sys
import traceback

import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.on_command_error = self._on_command_error

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

    async def _on_command_error(self, ctx, error):
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
