from sqlite3.dbapi2 import Timestamp
from discord.ext.commands import Cog, command
from discord import Colour, emoji, utils, Embed
from ..db import db
from random import randint
from datetime import datetime

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
        print(f"{__name__} cog ready")
    
    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.emoji.name == "\u2b50":
            #FIXME: Utilizar db.field no lugar de db.record. Não é necessário, é só para utilizar a db de maneira correta.
            hof_channel_id = db.record("SELECT HOF_channel_ID FROM Guild_Settings WHERE GuildID = ?", payload.guild_id)[0]
            print(f"New reaction detected. Server has HOF: {hof_channel_id}")

            if hof_channel_id:
                reaction_channel = self.bot.get_channel(payload.channel_id)
                reacted_message = await reaction_channel.fetch_message(payload.message_id)

                if reacted_message.author.bot:
                    await reacted_message.remove_reaction(payload.emoji, payload.member)

                
                elif not reaction_channel.is_nsfw():
                    msg_id = db.field("SELECT Root_message_ID FROM hall_of_fame WHERE Root_message_ID = ?", payload.message_id) or None

                    if utils.get(reacted_message.reactions, emoji="\u2b50").count > 0 and not msg_id:
                        hof_channel = self.bot.get_channel(hof_channel_id)
                        print("nova mensagem no HOF")
                        print(hof_channel)
                        print(payload.message_id)

                        embed = Embed(colour=0x000000,
                                     timestamp=datetime.utcnow())

                        #FIXME: só está aqui para referência futura.
                        # fields = [("Source", f"[Ir para mensagem]({reacted_message.jump_url})", False),
                        #           ("Conteúdo", reacted_message.content or "Imagem", False)]

                        if reacted_message.content:
                            embed.add_field(name="Disse:" ,value=reacted_message.content, inline=True)

                        embed.add_field(name="Source", value=f"[Ir para mensagem]({reacted_message.jump_url})", inline=False) 

                        if len(reacted_message.attachments):
                            embed.set_image(url=reacted_message.attachments[0].url)

                        embed.set_author(name=f"{reacted_message.author.display_name} ({reacted_message.author})", icon_url=reacted_message.author.display_avatar.url)
                        embed.set_footer(text=f"Todos os direitos reservados. NFT #{randint(10_000,999_999_999)}")

                        hof_message = await hof_channel.send(embed=embed)
                        
                        db.execute("INSERT INTO hall_of_fame(Root_message_ID, Hall_message_ID) VALUES (?, ?)", payload.message_id, hof_message.id)


async def setup(bot):
    await bot.add_cog(HOF(bot))