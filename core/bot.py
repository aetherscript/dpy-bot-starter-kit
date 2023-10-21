from __future__ import annotations

import os
import discord
import asyncio
from discord.ext import commands
from logging import getLogger; log = getLogger("Bot")

__all__ = (
    "Bot",
)

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("PREFIX"),
            intents=discord.Intents.all(),
            chunk_guild_at_startup=False
        )
    
    async def setup_hook(self):
        for f in os.listdir("./cogs"):
            if f == "__pycache__":
                continue
            try:
                await self.load_extension(f"cogs.{f}")
                log.info(f"Loaded cog {f}")
            except Exception as e:
                log.error(f"Failed to load cog {f}: {e}")

        await asyncio.sleep(5)
        synced_commands = await self.tree.sync()
        log.info(f"Successfully synced {len(synced_commands)} command(s).")

    async def on_ready(self) -> None:
        log.info(f"Logged in as {self.user} (ID: {self.user.id})")
    
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        if ctx.command is commands.hybrid_command:
            await ctx.reply("an error occured while processing your command.")
        embed = discord.Embed(title="Error", color=discord.Color.red())
        embed.description = f"```py\n{error}```"
        await ctx.reply(embed=embed)
        return


    async def on_application_command_error(self, ctx: commands.Context, error: Exception):
        embed = discord.Embed(title="Error", color=discord.Color.red())
        embed.description = f"```py\n{error}```"
        await ctx.reply(embed=embed)
