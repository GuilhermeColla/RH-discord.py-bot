from discord.ext.commands import Cog
from discord.ext.commands.core import command
from ..db import db

""" 
Esse Cog irá tomar conta dos canais que outros cogs podem precisar. Ele que
irá cuidar de escrever e atualizar a nossa database.
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
        print(f"{__name__} cog ready")
    

    # Commands
    @command(name="hall of fame", 
             aliases=["hof", "HOF", "starboard", "Starboard", "Hall of Fame"])
    async def set_hall_of_fame(self, ctx):

        """
        O canal de texto onde esse comando é invocado será utilizado pelo 
        bot para enviar as mensagens que obtiverem reações suficientes para
        entrar no corredor da fama.
        """
        print("guild_settings 'hall of fame' foi invocado pelo usuário")
        print(f"guild id: {ctx.guild.id}\nchannel: {self.bot.get_channel(ctx.channel.id)}")
        in_db = db.records("select GuildID from Guild_Settings")
        if (ctx.guild.id, ) in in_db:
            db.execute("UPDATE Guild_Settings SET HOF_channel_ID = ? WHERE GuildID = ?", ctx.channel.id, ctx.guild.id)
        else:
            db.execute("INSERT into Guild_Settings (GuildID, HOF_channel_ID) VALUES (?, ?)", ctx.guild.id, ctx.channel.id)
        db.commit()
        await ctx.reply(f"Hall of Fame definido para o canal {self.bot.get_channel(ctx.channel.id).mention}")


async def setup(bot):
    await bot.add_cog(GuildSettings(bot))