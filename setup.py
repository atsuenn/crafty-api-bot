import os
from dotenv import load_dotenv

discord_token = input("Enter your Discord bot token: ")
crafty_api_key = input("Enter your Crafty API key: ")
crafty_url = input("Enter Crafty URL (default https://127.0.0.1:8000): ") + "/api/v2/servers/"
server_id = input("Enter Crafty server ID: ")

env_content = f"""DISCORD_TOKEN={discord_token}
CRAFTY_TOKEN={crafty_api_key}
SERVER_ID={server_id}
CRAFTY_URL={crafty_url}
"""

with open(".env", "w") as f:
    f.write(env_content)

print("Created .env file successfully!")
os.system("cls")

def OpenMain():
    answer = input("Would you like to run the bot now? (Y/n)").lower()

    if answer == "y":
        os.system("cls")
        os.system("main.py")
    elif answer == "n":
        exit
    else:
        print("Invalid Option.")
        OpenMain()

OpenMain()
