import discord
client = discord.Client()

import urllib3
urllib3.disable_warnings() # Disables SSL console warning

full_dict = {} # Creates base dictionary
    # Entries will take the form {'user1':{'game1a':'game1a-friendcode', 'game1b':'game1b-friendcode'}, 'user2':{'game2a':'game2a-friendcode', 'game1b':'game1b-friendcode'}}

game_list = {'WII1':"Wii Friend Code 1", 'WII2':"Wii Friend Code 2", 'WII3':"Wii Friend Code 3", 'MKW':"Mario Kart Wii (Wiimmfi)", 'ACCF':"Animal Crossing: City Folk (Wiimmfi)", 'SSBB':"Super Smash Bros. Brawl (Wiimmfi)"} # list of supported games

tokenfile = open('token.txt') # Private bot token file
token = tokenfile.read()[:-1]
tokenfile.close()

command_prefix = '!'
command_list = ['setCode','getAllGames','getAllUsers','getUsersOf','getCode','getUsersAndCodesOf','help','terminate']

@client.event
async def on_message(message):
    author = str(message.author)
    content = message.content
    print(message)
    print(author + ':', content)
    if content[0] == command_prefix:
        if content[1:].split(" ")[0] in command_list:
            execute_command(content[1:],author)
        else: # If the user called the bot but with an invalid command
            print("Error: Invalid command", content[1:])

@client.event
async def on_ready(): # When the bot launches
    print('Ready!')
    print('User:', client.user.name)
    print('Client ID:', client.user.id)
    print('------')
    print(client)

def execute_command(command_entered,command_author): # command syntax checker / launcher
    user_args = command_entered.split(" ")
    base_command = user_args[0]
    if base_command == 'setCode':
        if len(user_args) == 3:
            setCode(command_author, user_args[1], user_args[2])
        else:
            print("Error: Incorrect number of arguments")
    elif base_command == 'getAllGames':
        getAllGames()
    elif base_command == 'getAllUsers':
        getAllUsers()
    elif base_command == 'getUsersOf':
        if len(user_args) == 2:
            getUsersOf(user_args[1])
        else:
            print("Error: Incorrect number of arguments")
    elif base_command == 'getCode':
        if len(user_args) == 3:
            getCode(user_args[1], user_args[2])
        else:
            print("Error: Incorrect number of arguments")
    elif base_command == 'getUsersAndCodesOf':
        if len(user_args) == 2:
            getUsersAndCodesOf(user_args[1])
        else:
            print("Error: Incorrect number of arguments")
    elif base_command == 'help':
        help()
    elif base_command == 'terminate':
        terminate(command_author)

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

def terminate(): # Kills the bot (valid only if used by devs)
    pass

def main():
    client.run(token) # Log the bot into discord and run

if __name__ == '__main__': # If run as the main program
    main()
