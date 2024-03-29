from apscheduler.schedulers.asyncio import AsyncIOScheduler
from os import listdir
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands.errors import CommandNotFound
from discord.flags import Intents
from ..db import db

PREFIX = "rh"
OWNER_IDS = [229057896158068736]
COGS = [filename[:-3] for filename in listdir("./lib/cogs") 
        if filename.endswith(".py")]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.scheduler = AsyncIOScheduler()
        
        db.autosave(self.scheduler)
        super().__init__(
            command_prefix=PREFIX,
            owner_ids=OWNER_IDS,
            strip_after_prefix=True,
            intents=Intents.all()
        )

    async def setup(self):
        #TODO: Quando redacted estiver funcionando, remover esse if/else.
        for cog in COGS:
            if not cog.startswith("beta"):
                await self.load_extension(f"lib.cogs.{cog}")
                print(f"{cog} cog loaded")

        print("setup complete")

    async def run(self, version):
        self.VERSION = version

        print("running setup...")
        await self.setup()

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        
        print("running bot...")
        await super().start(self.TOKEN, reconnect=True)
    
    async def on_connect(self):
        print("bot connected")
    
    async def on_disconnect(self):
        print("bot disconnected")

    """ async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            print(args)
            await args[0].send("Something went wrong.")
        else:
            print("An error occured.") """

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send("Comando não encontrado.")
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc
    
    async def on_ready(self):
        if not self.ready:
            self.scheduler.start()
            self.ready = True
            print("bot ready")
        else:
            print("bot reconnected")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)


bot = Bot()
