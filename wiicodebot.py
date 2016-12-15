import os
import datetime

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
            await execute_command(message,content[1:],author)
        else: # If the user called the bot but with an invalid command
            await client.send_message(message.channel,"Error: Invalid command " + content)
            print("Error: Invalid command " + content)

@client.event
async def on_ready(): # When the bot launches
    print('Ready!')
    print('User:', client.user.name)
    print('Client ID:', client.user.id)
    print('------')
    print(client)

async def execute_command(message,command_entered,command_author): # command syntax checker / launcher
    user_args = command_entered.split(" ")
    base_command = user_args[0]
    arg_error_usrmsg = "Error: Incorrect number of arguments. Please consult " + str(command_prefix) + "help"
    if base_command == 'setCode':
        if len(user_args) == 3:
            await setCode(message,command_author, user_args[1], user_args[2])
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command == 'getAllGames':
        if len(user_args) == 1:
            await getAllGames(message)
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command == 'getAllUsers':
        if len(user_args) == 1:
            await getAllUsers(message)
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command == 'getUsersOf':
        if len(user_args) == 2:
            await getUsersOf(message,user_args[1])
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command == 'getCode':
        if len(user_args) == 3:
            await getCode(message,user_args[1], user_args[2])
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command == 'getUsersAndCodesOf':
        if len(user_args) == 2:
            await getUsersAndCodesOf(message,user_args[1])
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command == 'help':
        if len(user_args) == 1:
            await help(message)
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command == 'terminate':
        if len(user_args) == 1:
            await terminate(message,command_author)
        else:
            await client.send_message(message.channel,arg_error_usrmsg)


async def setCode(message,username, game, code): # Lets the user set his/her code for a specific game
    if game in game_list.keys():
        if username not in full_dict.keys():
            full_dict[username] = {}
        full_dict[username][game] = code
        await client.send_message(message.channel,code + " successfully added for " + game + " for " + username[:-5])
    else:
        await client.send_message(message.channel,"Error: Game not in database. Please consult " + command_prefix + "help or " + command_prefix + "getAllGames")

async def getAllGames(message): # Displays a list of the supported games by the bot
    await client.send_message(message.channel,"Currently Supported Games:")
    for element in sorted(game_list.keys()):
        await client.send_message(message.channel," - " + element + ": " + game_list[element])

async def getAllUsers(message): # Displays a list of all users with registered friend codes
    await client.send_message(message.channel,"Currently Registered Users:")
    for element in sorted(full_dict.keys()):
        await client.send_message(message.channel," - " + element[:-5])

async def getUsersOf(message,game): # Displays list of users with friend codes registered for a specific game
    users_with_game = []
    for element in sorted(full_dict.keys()):
        user_data = full_dict[element]
        if game in sorted(user_data.keys()):
            users_with_game.append(element[:-5])
    if len(users_with_game) == 0:
        await client.send_message(message.channel,"No Users Registered with " + game_list[game])
    else:
        await client.send_message(message.channel,"Users Registered with " + game_list[game] + ":")
        for element in users_with_game:
            await client.send_message(message.channel," - " + element)

async def getCode(message,username, game): # Returns the friend code of a specific user and game
    if game in game_list.keys():
        if username in full_dict.keys():
            if game in full_dict[username].keys():
                await client.send_message(message.channel,full_dict[username][game])
            else:
                await client.send_message(message.channel,"Error: User has not registered with that game")
        else:
            await client.send_message(message.channel,"Error: User has no registered friend codes")
    else:
        await client.send_message(message.channel,"Error: Game not in database. Please consult " + command_prefix + "help or " + command_prefix + "getAllGames")

async def getUsersAndCodesOf(message,game): # Displays list of users and friend codes for a specific game
    users_with_game = []
    for element in sorted(full_dict.keys()):
        user_data = full_dict[element]
        if game in sorted(user_data.keys()):
            users_with_game.append(element)
    if len(users_with_game) == 0:
        await client.send_message(message.channel,"No Users Registered with " + game_list[game])
    else:
        await client.send_message(message.channel,"Users Registered with " + game_list[game] + ":")
        for element in users_with_game:
            await client.send_message(message.channel," - " + element[:-5] + ": " + full_dict[element][game])

async def help(message): # Bot user documentation
    pass

def saveBackup(): # Saves a backup of user data
    if os.path.isfile('user_dictionary.txt'): # If a backup already exists, rename it with the date/time of replacement
        now = datetime.datetime.now()
        os.rename('user_dictionary.txt', 'user_dictionary_' + now.strftime("%Y-%m-%d_%H-%M-%S") + '-' + str(now.microsecond) + '.txt')
    backup_file = open('user_dictionary.txt','w') # Create a new writable backup file
    for element in full_dict.keys(): # Backup user data
        backup_file.write(str(element) + ':' + str(full_dict[element]))

def loadBackup(backupfile): # Loads backed up user data into the dictionary
    pass

async def terminate(): # Kills the bot (valid only if used by devs)
    # Save the user dictionary to a backup file user_dictionary.txt, then use exit()
    if len(full_dict) > 0: # If there is data to backup
        saveBackup()
    exit()

def main():
    if os.path.isfile('user_dictionary.txt'): # If a backup of the user dictionary exists, load it
        loadBackup(open('user_dictionary.txt','r'))
    
    client.run(token) # Log the bot into discord and run

if __name__ == '__main__': # If run as the main program
    main()
