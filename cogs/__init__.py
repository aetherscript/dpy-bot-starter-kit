from .utility import Utility
from core import Bot

async def setup(bot: Bot):
    await bot.add_cog(Utility(bot))
  
