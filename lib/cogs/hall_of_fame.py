from discord.ext.commands import Cog, command

""" 
Esse Cog implementa o hall of fame também conhecido como "star channel".
Mensagens que receberem certa quantidade de reações com o emote de estrela
(:star:) serão enviadas para um canal específico.
"""


class HOF(Cog):
    def __init__(self, bot):
        self.bot = bot

    # Event
    @Cog.listener()
    async def on_ready(self):
        print("Hof cog ready")
    
    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        pass





def setup(bot):
    bot.add_cog(HOF(bot))