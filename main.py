import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", help_command=None, intents=discord.Intents.all())

TOKEN = input("Please enter your bot token:")




@bot.event
async def on_ready():
    print("servers")
    for guild in bot.guilds:
        print(f"- {guild.name} ({guild.id}), {guild.member_count} members")

bot.run(TOKEN)
