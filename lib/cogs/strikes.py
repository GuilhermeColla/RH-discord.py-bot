from discord.ext.commands import Cog, command

"""
Esse Cog implementa o jogo dos strikes.
-> Ao tomar 3 strikes o usuário tem seu microfone desativado por 24 horas contadas
a partir do momento que o terceiro strike foi dado.
-> Cada usuário pode dar 1 strike a cada 24 horas.
-> Cada strike deve ser dado por usuários diferentes - evitando que um único 
usuário possa desativar o microfone de alguém a cada 3 dias.
"""

class Strikes(Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events
    @Cog.listener()
    async def on_ready(self):
        print("Strikes cog ready")

    # Commands
    @command()
    async def strike(self, ctx, *reason):
        print(reason.join(' '))
        
def setup(bot):
    bot.add_cog(Strikes(bot))