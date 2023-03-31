import discord

intents = discord.Intents.default()
intents.members = True

TOKEN = input("Please enter your bot token:")


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot is ready")
    print("Servers connected to:")
    for guild in client.guilds:
        print(f"- {guild.name} ({guild.id}), {guild.member_count} members")

client.run(TOKEN)
