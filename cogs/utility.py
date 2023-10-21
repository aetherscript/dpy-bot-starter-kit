from __future__ import annotations

from core import Bot
import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="ping", aliases=["p"])
    async def ping(self, ctx: commands.Context):
        """Replies with Pong and Bot Latency."""
        embed = discord.Embed(description=f"Pong! {round(self.bot.latency*1000)}ms.")
        await ctx.send(embed=embed)
