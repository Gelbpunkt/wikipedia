import aiohttp
import aiowiki
from discord.ext import commands

import config


class Wikipedia(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.session = None

    def __repr__(self):
        return "Wikipedia Botto"

    async def start(self):
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.wiki = aiowiki.Wiki.wikipedia("en", session=self.session)

        for ext in config.exts:
            self.load_extension(ext)

        await super().start(config.token, bot=True)


if __name__ == "__main__":
    Wikipedia(
        command_prefix=commands.when_mentioned_or("wiki "), case_insensitive=True
    ).run()
