import discord
client = discord.Client()

import urllib3
urllib3.disable_warnings() # Disables SSL console warning

full_dict = {} # Creates base dictionary
game_list = {'WII1':'Wii Friend Code 1', 'WII2':'Wii Friend Code 2', 'WII3':'Wii Friend Code 3', 'MKW':'Mario Kart Wii (Wiimmfi)', 'ACCF':'Animal Crossing: City Folk (Wiimmfi)', 'SSBB':'Super Smash Bros. Brawl (Wiimmfi)'] # list of supported games

token = 'MjU4ODg3MjMzODA3OTc0NDAw.CzQDQQ.LH-rOrbRTZ_DxlGcfevg6j3AgG4' # Bot Token

command_prefix = '!'
command_list = ['setCode','getAllGames','getAllUsers','getUsersOf','getCode','getUsersAndCodesOf','help']

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print(str(message) + ':', content)
    if content[0] == command_prefix:
        if content[1:] in command_list:
            pass
        else: # If the user called the bot but with an invalid command
            print("Error: Invalid command", content[1:])

@client.event
async def on_ready(): # When the bot launches
    print('Ready!')
    print('User:', client.user.name)
    print('Client ID:', client.user.id)
    print('------')
    print(client)

def setCode(username, game, code): # Lets the user set his/her code for a specific game
    pass

def getAllGames(): # Displays a list of the supported games by the bot
    for element in sorted(game_list.keys):
        print(game_list[element])

def getAllUsers(): # Displays a list of all users with registered friend codes
    pass

def getUsersOf(game): # Displays list of users with friend codes registered for a specific game
    pass

def getCode(username, game): # Returns the friend code of a specific user and game
    pass

def getUsersAndCodesOf(game): # Displays list of users and friend codes for a specific game
    pass

def help(): # Bot user documentation
    pass


def main():
    client.run(token) # Log the bot into discord and run

if __name__ == '__main__': # If run as the main program
    main()
