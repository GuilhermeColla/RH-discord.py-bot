from discord.ext.commands import Cog, command

""" 
Implementa um sistema para carregar e descarrregar Cogs.
Isso possibilita que cogs possam ser modificados e atualizados com o bot em
funcionamento (restartless patches).
"""


class ManualLoadUnload(Cog):
    def __init__(self, bot):
        self.bot = bot

    # Event
    @Cog.listener()
    async def on_ready(self):
        print(f"{__name__} cog ready")
    

    # Commands
    @command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f"lib.cogs.{extension}")
        print(f"Loaded {extension}")

    @command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f"lib.cogs.{extension}")
        print(f"Unloaded {extension}")

    @command()
    async def reload(self, ctx, extension):
        self.bot.unload_extension(f"lib.cogs.{extension}")
        self.bot.load_extension(f"lib.cogs.{extension}")
        print(f"Reloaded {extension}")



def setup(bot):
    bot.add_cog(ManualLoadUnload(bot))