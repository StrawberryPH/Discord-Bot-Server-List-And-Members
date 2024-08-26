import discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())

TOKEN = input("Please enter your bot token:")




@bot.event
async def on_ready():
    print("servers")
    for guild in client.guilds:
        print(f"- {guild.name} ({guild.id}), {guild.member_count} members")

bot.run(TOKEN)
