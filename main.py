# Crafty-API-Bot

import discord
from discord import app_commands
from discord.ext import commands

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Config for crafty API
craftyAPIToken = os.getenv("CRAFTY_TOKEN")
headers = {"Authorization": f"Bearer {craftyAPIToken}"}
serverID = os.getenv("SERVER_ID")
defaultURL = os.getenv("CRAFTY_URL") + f"{serverID}/"

print(f"Default URL: {defaultURL}")

#Discord Bot Config
discordBotToken = os.getenv("DISCORD_TOKEN")
commandPrefix = "!"


# First Intialisation stage
class Client(commands.Bot):
    def __init__(self, i: discord.Intents):
        super().__init__(command_prefix=commandPrefix, intents=intents)

    


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = Client(i=intents)

# Syncing command
@bot.command()
async def sync(ctx):
    """Syncing command for loading / commands onto discord server"""
    await bot.tree.sync()
    print("Synced with playground")
    await ctx.send("Sync Complete, please reload (CTRL+R).")

# Github Link
@bot.command()
async def github(ctx):
    """Takes you to the GitHub page"""
    await ctx.send("Link to project GitHub page: https://github.com/atsuenn/crafty-api-bot")


#
# Crafty API Bot commands
#

@bot.tree.command(name="start", description="Starts server")
async def start_server(interaction: discord.Interaction):
    """Starts minecraft server by sending API request to your craft controller instance."""
    url = defaultURL + "action/start_server"

    response = requests.post(url, headers=headers, verify=False)

    await interaction.response.send_message("Starting...")

@bot.tree.command(name="stop", description="Stops server")
async def start_server(interaction: discord.Interaction):
    """Stops minecraft server by sending API request to your craft controller instance."""
    url = defaultURL + "action/stop_server"

    response = requests.post(url, headers=headers, verify=False)

    await interaction.response.send_message("Stopping...")

@bot.tree.command(name="sendcommand", description="Send a terminal command to your server")
async def send_command(interaction: discord.Interaction, cmd: str):
    """Sends commands by sending an API requests with your command attached."""
    url = defaultURL + "stdin"
    print(url)

    response = requests.post(url, headers=headers, data=cmd, verify=False)
    await interaction.response.send_message(f"Sending command: {cmd}")


if __name__ == "__main__":
    # initalising bot
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user} (ID: {bot.user.id})")
        print("------")
    bot.run(discordBotToken)

#
# Code written by atsuenn
# https://github.com/atsuenn
#
