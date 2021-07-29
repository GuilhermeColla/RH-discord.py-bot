from discord.ext.commands import Cog
from discord.ext.commands.core import command
from ..db import db

""" 
Esse Cog irá tomar conta dos canais que outros cogs podem precisar.
Atualmente teremos 2 canais importantes:
1*-) Canal para o Hall of Fame;
2-) Canal para comandos de bot.

Os números marcados com asterisco são indispensáveis quando seus respectivos
cogs serão utilizados, enquanto os sem, são facultativos.
"""


class GuildSettings(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Events
    @Cog.listener()
    async def on_ready(self):
        print("Guild settings ready")
    
    # Commands
    @command(name="set", aliases=["setting", "config"])
    async def modify_setting(self, setting, ctx):
        pass
        db.record("alter table Guild_Settings add ")



def setup(bot):
    bot.add_cog(GuildSettings(bot))