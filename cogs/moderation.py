import discord
from discord.ext import commands
from discord import app_commands

class ModerationCog(commands.Cog):

    # Au chargement du bot -> cog
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        # anti insulte
        words_blacklist = ['crapouille', 'gougnafier', 'malotru', 'garnement']

        # recuperer chaque mot
        for mot in message.content.split():
            if mot in words_blacklist:
                await message.delete()
                await message.channel.send("Attention à ton langage !")
                break

    @app_commands.command(name="kickback", description="J'te kick")
    async def kickback_command(interaction: discord.Interaction, member: discord.Member):
        # --> /ciao @pseudo
        await member.send('Tu t\'es fait kick, reviens même pas !')
        await member.kick(reason="Pk tu vis ?")
        await interaction.response.send_message("Le membre a été kick nickel ! Ca dégage")

# Préparer une fonction setup qui va enregistrer le cog dans le bot
async def setup(client):
    await client.add_cog(ModerationCog(client))