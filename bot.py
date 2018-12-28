import discord
import aiowiki
import aiohttp
import asyncio
from discord.ext import commands

import config


class Wikipedia(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.owners = [356091260429402122, 340745895932854272]
        self.session = None

    def __repr__(self):
        return "Wikipedia Botto"

    async def start(self):
        self.session = aiohttp.ClientSession(loop=self.loop)

        for ext in config.exts:
            self.load_extension(ext)

        super().run(config.token, bot=True)


if __name__ == "__main__":
    Wikipedia(
        command_prefix=commands.when_mentioned_or("wiki "), case_insensitive=True
    ).run()
