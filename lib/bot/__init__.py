from apscheduler.schedulers.asyncio import AsyncIOScheduler
from os import listdir
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands.errors import CommandNotFound
from discord.flags import Intents
from ..db import db

PREFIX = "rh"
OWNER_IDS = [229057896158068736]
COGS = [filename[:-3] for filename in listdir(".\lib\cogs") 
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

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} cog loaded")

        print("setup complete")

    def run(self, version):
        self.VERSION = version

        print("running setup...")
        self.setup()

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        
        print("running bot...")
        super().run(self.TOKEN, reconnect=True)
    
    async def on_connect(self):
        print("bot connected")
    
    async def on_disconnect(self):
        print("bot disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            print(args)
            await args[0].send("Something went wrong.")
        else:
            print("An error occured.")

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send("Escreve direito, caraio")
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc
    
    async def on_ready(self):
        if not self.ready:
            self.command_channel = self.get_channel(291738640906977290)        
            self.scheduler.start()
            self.ready = True
            print("bot ready")
        else:
            print("bot reconnected")

    async def on_message(self, message):
        if not message.author.bot:
            if self.command_channel and message.content.startswith(PREFIX):
                if message.channel.id == self.command_channel.id:
                    await self.process_commands(message)
                else:
                    await message.reply(f"{self.command_channel.mention}?")
            if message.content == "pula?":
                await message.channel.send("pa caraio :^)")

    async def on_raw_reaction_add(self, payload):
        pass


bot = Bot()
