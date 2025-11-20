# Installation

**First make sure you have screen installed, if not:**
```
sudo apt update
```
**Then run:**
```
sudo apt install screen
```

**Install complete!**

# Use

**Starting a screen session:**
```
screen -S myBot
```

**Creating a new python virtual env:**
```
source venv/bin/activate
```

**Then run main.py:**
```
python3 main.py
```
*If it spits an import error back at you, do pip3 and install the necessary requirements again.*

To detach from the screen session (you can re-enter later) press ``CTRL + A`` then press ``D`` and you're done, the bot is now running headless!

# Re-entering

**To re-enter the screen session:**
```
screen -r myBot
```

**If you forgot the session name, run:**
```
screen -ls
```
**for a full list of screen sessions.**
