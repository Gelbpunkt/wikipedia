import discord
from discord.ext import commands


class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def search(self, ctx, *, page_title: str):
        """Searches Wikipedia for an entry."""
        pages = await self.bot.wiki.opensearch(page_title)
        if not pages:
            return await ctx.send("No results.")
        best_match = pages[0]
        text_of_match, match_urls, images = (
            await best_match.summary(),
            await best_match.urls(),
            await best_match.media(),
        )
        embed = discord.Embed(
            title=best_match.title,
            url=match_urls.view,
            description=text_of_match[:1999],
        )
        embed.set_thumbnail(url=images[0])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Search(bot))
