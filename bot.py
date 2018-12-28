import discord
import aiowiki
import aiohttp
import asyncio
from discord.ext import commands

import config

bot = commands.Bot(command_prefix="wiki ", case_insensitive=True)


async def start():
    bot.session = aiohttp.ClientSession(loop=bot.loop)
    bot.wiki = aiowiki.Wiki.wikipedia("en", session=bot.session)
    for ext in config.exts:
        bot.load_extension(ext)
    await bot.start(config.token)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start())
