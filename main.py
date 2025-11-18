import requests
import os

import discord 
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Config for crafty API
craftyAPIToken = os.getenv("CRAFTY_TOKEN")
headers = {"Authorization": f"Bearer {craftyAPIToken}"}
serverID = os.getenv("SERVER_ID")
defaultURL = os.getenv("CRAFTY_URL") + f"{serverID}/"

print(defaultURL)

discordBotToken = os.getenv("DISCORD_TOKEN")
commandPrefix = "!"

intents = discord.Intents.default()
intents.message_content = True

#Init DC Bot
bot = commands.Bot(command_prefix=commandPrefix, intents=intents)

@bot.command()
async def start(ctx):
    url = defaultURL + "action/start_server"

    response = requests.post(url, headers=headers, verify=False)
    await ctx.send("Starting...")

@bot.command()
async def stop(ctx):
    url = defaultURL + "action/stop_server"
    
    response = requests.post(url, headers=headers, verify=False)
    await ctx.send("Stopping...")

@bot.command()
async def send_command(ctx, cmd):
    url = defaultURL + "stdin"
    print(url)

    response = requests.post(url, headers=headers, data=cmd, verify=False)
    await ctx.send("Sending...")

for command in bot.commands:
    print(command)

bot.run(discordBotToken)
