import os


def Installer():
    answer = input("Would you like to install the necessary requirements?(Y/n)").lower()

    if answer == "y":
        os.system("pip install discord.py python-dotenv requests")
    elif answer == "n":
        exit
    else:
        print("Invalid Option.")
        Installer()

Installer()