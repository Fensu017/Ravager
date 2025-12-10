from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands
import os
import discord
import random


intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
tree_commands = client.tree

@tree_commands.command(name="csm", description="Attendre le prochain chapitre CSM ensemble")
async def csm_command(interaction: discord.Interaction):
    await interaction.response.send_message("Prochain chapitre CSM dans 30 minutes ! Préparez-vous ! https://mangaplus.shueisha.co.jp/viewer/7002257")

@tree_commands.command(name="gamesaward", description="Top 5 des jeux de l'année")
async def gamesaward_command(interaction: discord.Interaction):
    embed = discord.Embed(title="Top 5 des jeux de l'année")
    embed.add_field(name="top 1", value="Ghost of Yotei")
    embed.add_field(name="top 2", value="Clair Obscur : Expedition 33")
    embed.add_field(name="top 3", value="Elden Ring : NightReign")
    embed.add_field(name="top 4", value="Hollow Knight: Silksong")
    embed.add_field(name="top 5", value="Hades II: Infernal Machine")
    await interaction.response.send_message(embed=embed)

@tree_commands.command(name="memes", description="Générateur de memes")
async def memes_command(interaction: discord.Interaction):
    meme = [
        "https://media.tenor.com/DfbrUNgzFJoAAAAM/gogeta-dragon-ball.gif",
        "https://media.tenor.com/9YXmEfHqaVYAAAAM/ul-ssgss-gogeta-unique-gauge.gif",
        "https://preview.redd.it/best-scream-v0-p86nzf867sjc1.jpeg?format=pjpg&auto=webp&s=d58152fb3c6b50aab5f117f338eec39dc92b4c55"
    ]

    meme = random.choice(meme)
    await interaction.response.send_message(meme)

@client.event
async def on_ready():
    # Enregistrer les cogs
    await client.load_extension('cogs.moderation')
    await client.load_extension('cogs.legends')  # Système de collection de cartes
    await tree_commands.sync()  # Synchroniser les commandes avec le serveur Discord
    print(f'Une arrivée fulgurante ! {client.user}')
    print(f'✅ Système de Failles des Légendes chargé !')

@client.event
async def on_member_join(member : discord.Member):
    print(f'{member} a rejoint le serveur.')

    # envoyer un message dans le salon nouveau-membres
    member_channel_id =  1299769029124292701
    member_channel = client.get_channel(member_channel_id)
    await member_channel.send(f'Bienvenue sur le serveur, {member.mention} !')
    
    # Envoyer un message privé de bienvenue
    await member.send('Bienvenue sur le serveur !')

client.run(os.getenv("DISCORD_TOKEN"))