# Crafty API Bot

A nice easy python based discord bot for interacting with Craft Controllers API.

# Features
- Start/Stop
- Send Commands
- Uses Discord / commands
- More soon, maybe.
# Installation
***!! MAKE SURE YOU FIRST HAVE PYTHON INSTALLED !!***

Either download the source files manually and open installation.py or do:
``` 
git clone https://github.com/atsuenn/crafty-api-bot.git
```

Then once it has cloned, open the folder and run installation.py and let it install the necessary libraries, if it *doesn't work* you need to install:
```
pip install discord
pip install requestsa
pip insatll dotenv
```

Once you have the necessary libraries, you can then run setup.py where it will ask you for your discord token *(go to the discord dev portal and make a new application, this is not a tutorial for setting that up)*, your crafty API key *(can be found in your user settings)*, and your crafty machines IP and correct port *(if you're running this on the same machine as crafty the ip can just be* https://localhost:portnumber), then finally your server UUID which can be found in your crafty UI when in the terminal section.

# Usage
**On windows:**
Double click the main.py or open it using terminal.

**On Linux:**
```
python main.py
```

Once the code is running and has connected to discord, you then need to go to a channel in which your server is in and run ``!sync`` which will then sync the / commands to your server.

Now you can use the bot !!