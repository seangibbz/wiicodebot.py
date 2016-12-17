import os
import datetime

import discord
client = discord.Client()

import urllib3
urllib3.disable_warnings() # Disables SSL console warning


full_dict = {} # Creates base dictionary
    # Entries will take the form {'user1':{'game1a':'game1a-friendcode', 'game1b':'game1b-friendcode'}, 'user2':{'game2a':'game2a-friendcode', 'game1b':'game1b-friendcode'}}

game_list = {'WII1':"Wii Friend Code 1", 'WII2':"Wii Friend Code 2", 'WII3':"Wii Friend Code 3", 'MKW':"Mario Kart Wii (Wiimmfi)", 'ACCF':"Animal Crossing: City Folk (Wiimmfi)", 'SSBB':"Super Smash Bros. Brawl (Wiimmfi)", 'TC2':"The Conduit 2", 'PBR':"Pokémon Battle Revolution"} # list of supported games


tokenfile = open('token.txt') # Private bot token file
token = tokenfile.read()[:-1]
tokenfile.close()

command_prefix = '!'
command_list = ['setCode','getAllGames','getAllUsers','getUsersOf','getCode','getUsersAndCodesOf','help','terminate','backup','getUserCodes']


@client.event
async def on_message(message):
    author = str(message.author)
    content = message.content
    print(message)
    print(author + ':', content)
    if (content[0] == command_prefix) and (message.author != client.user):
        if content[1:].split(" ")[0].lower() in [x.lower() for x in command_list]:
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
    if base_command.lower() == 'setcode':
        if len(user_args) == 3:
            await setCode(message,command_author, user_args[1], user_args[2])
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command.lower() == 'getallgames':
        if len(user_args) == 1:
            await getAllGames(message)
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command.lower() == 'getallusers':
        if len(user_args) == 1:
            await getAllUsers(message)
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command.lower() == 'getusersof':
        if len(user_args) == 2:
            await getUsersOf(message,user_args[1])
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command.lower() == 'getcode':
        if len(user_args) == 3:
            await getCode(message,user_args[1], user_args[2])
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command.lower() == 'getusersandcodesof':
        if len(user_args) == 2:
            await getUsersAndCodesOf(message,user_args[1])
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command.lower() == 'help':
        if len(user_args) == 1:
            await help(message)
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command.lower() == 'terminate':
        if len(user_args) == 1:
            await terminate(message,command_author)
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command.lower() == 'backup':
        if len(user_args) == 1:
            await backup(message,command_author)
        else:
            await client.send_message(message.channel,arg_error_usrmsg)
    elif base_command.lower() == 'getusercodes':
        if len(user_args) == 2:
            await getUserCodes(message,user_args[1])
        else:
            await client.send_message(message.channel,arg_error_usrmsg)


async def setCode(message,username, game, code): # Lets the user set his/her code for a specific game
    if game in game_list.keys():
        if username not in full_dict.keys():
            full_dict[username] = {}
        full_dict[username][game] = code
        await client.send_message(message.channel,code + " successfully added as " + game_list[game] + " for " + username[:-5])
    else:
        await client.send_message(message.channel,"Error: Game not in database. Please consult " + command_prefix + "getAllGames")


async def getAllGames(message): # Displays a list of the supported games by the bot
    output_txt = "Currently Supported Games:"
    
    for element in sorted(game_list.keys()):
        output_txt = output_txt + '\n' + " - " + element + ": " + game_list[element]
    await client.send_message(message.channel,output_txt)


async def getAllUsers(message): # Displays a list of all users with registered friend codes
    if len(full_dict) > 0:
        output_txt = "Currently Registered Users:"
        for element in sorted(full_dict.keys()):
            output_txt = output_txt + '\n' + " - " + element[:-5]
        await client.send_message(message.channel,output_txt)
    else:
        await client.send_message(message.channel,"No Currently Registered Users")


async def getUsersOf(message,game): # Displays list of users with friend codes registered for a specific game
    users_with_game = []
    for element in sorted(full_dict.keys()):
        user_data = full_dict[element]
        if game in sorted(user_data.keys()):
            users_with_game.append(element[:-5])
    if len(users_with_game) == 0:
        await client.send_message(message.channel,"No Users Registered with " + game_list[game])
    else:
        output_txt = "Users Registered with " + game_list[game] + ":"
        for element in users_with_game:
            output_txt = output_txt + '\n' + " - " + element
        await client.send_message(message.channel,output_txt)

async def getUserCodes(message,username): # Displays list of users with friend codes registered for a specific game
    if username[1] == '@':
        good_user = await client.get_user_info(username[2:-1])
        good_username = str(good_user)
    else:
        good_username = username
    user_data = full_dict[good_username]
    game_result = "List of games for user " + good_username[:-5] + ":"
    for element in sorted(user_data.keys()):
        game_result = game_result + '\n' + game_list[element] + ": " + user_data[element]
    await client.send_message(message.channel,game_result)



async def getCode(message,username, game): # Returns the friend code of a specific user and game
    if username[1] == '@':
        good_user = await client.get_user_info(username[2:-1])
        good_username = str(good_user)
    else:
        good_username = username

    if game in game_list.keys():
        if good_username in full_dict.keys():
            if game in full_dict[good_username].keys():
                await client.send_message(message.channel,game_list[game] + " code for " + good_username[:-5] + ": " + full_dict[good_username][game])
            else:
                await client.send_message(message.channel,"Error: User " + good_username + " has not registered with that game")
        else:
            await client.send_message(message.channel,"Error: User " + good_username + " has no registered friend codes")
    else:
        await client.send_message(message.channel,"Error: Game " + game + " not in database. Please consult " + command_prefix + "getAllGames")


async def getUsersAndCodesOf(message,game): # Displays list of users and friend codes for a specific game
    users_with_game = []
    for element in sorted(full_dict.keys()):
        user_data = full_dict[element]
        if game in sorted(user_data.keys()):
            users_with_game.append(element)
    if len(users_with_game) == 0:
        await client.send_message(message.channel,"No Users Registered with " + game_list[game])
    else:
        output_txt = "Users Registered with " + game_list[game] + ":"
        for element in users_with_game:
            output_txt = output_txt + '\n' + " - " + element[:-5] + ": " + full_dict[element][game]
        await client.send_message(message.channel,output_txt)


async def help(message): # Bot user command documentation (!terminate and !backup excluded as they are dev commands)
    output_txt = "Available commands:"
    output_txt = output_txt + '\n' + " - " + command_prefix + "help: Displays a list of available commands"
    output_txt = output_txt + '\n' + " - " + command_prefix + "setCode <GAMEID> <CODE>: Set a code for yourself for a specific game (e.g. " + command_prefix + "setCode WII1 8045-7532-5656-2676)"
    output_txt = output_txt + '\n' + " - " + command_prefix + "getCode <USER MENTION> <GAMEID>: Get a code for a specific user/game (e.g. " + command_prefix + "setCode @seangibbz#5609 WII1)"
    output_txt = output_txt + '\n' + " - " + command_prefix + "getAllGames: Get a list of all short-hand game codes
    output_txt = output_txt + '\n' + " - " + command_prefix + "getAllUsers: Get a list of all users with at least one registered friend code
    output_txt = output_txt + '\n' + " - " + command_prefix + "getUsersOf <GAMEID>: Get a list of users who have registered a code for a specific game (e.g. " + command_prefix + "getUsersOf WII1)"
    output_txt = output_txt + '\n' + " - " + command_prefix + "getUsersAndCodesOf <GAMEID>: Get a list of users who have registered a code for a specific game, as well as their corresponding friend codes (e.g. " + command_prefix + "getUsersAndCodesOf WII1)"
    output_txt = output_txt + '\n' + " - " + command_prefix + "getUserCodes <USER MENTION>: Get a list of all registered friend codes for a specific user (e.g. " + command_prefix + "getUserCodes @seangibbz#5609)"
    await client.send_message(message.channel,output_txt)


def saveBackup(): # Saves a backup of user data
    if os.path.isfile('user_dictionary.txt'): # If a backup already exists, rename it with the date/time of replacement
        now = datetime.datetime.now()
        os.rename('user_dictionary.txt', 'user_dictionary_' + now.strftime("%Y-%m-%d_%H-%M-%S") + '-' + str(now.microsecond) + '.txt')
    backup_file = open('user_dictionary.txt','w') # Create a new writable backup file
    for element in full_dict.keys(): # Backup user data
        backup_file.write(str(element) + ':' + str(full_dict[element]) + '\n')


def loadBackup(backupfile): # Loads backed up user data into the dictionary
    for line in backupfile:
        userpair = line.strip('\n').strip('}').split('{')
        user_value = userpair[0][:-1]
        full_dict[user_value] = {}
#        print("Loading user",user_value, "from backup")
        game_entries = userpair[1].split(', ')
        for element in game_entries:
            indv_entry = element.split(': ')
            full_dict[user_value][indv_entry[0].strip('\'')] = indv_entry[1].strip('\'')

async def backup(message,message_author): # Kills the bot (valid only if used by devs)
    # Save the user dictionary to a backup file user_dictionary.txt, then use exit()
    if len(full_dict) > 0: # If there is data to backup
        await client.send_message(message.channel,"Creating Backup...")
        saveBackup()
        await client.send_message(message.channel,"Backup Created")
    else:
        await client.send_message(message.channel,"Error: No data to backup.")


async def terminate(message,message_author): # Kills the bot (valid only if used by devs)
    # Save the user dictionary to a backup file user_dictionary.txt, then use exit()
    if len(full_dict) > 0: # If there is data to backup
        await client.send_message(message.channel,"Creating Backup...")
        saveBackup()
        await client.send_message(message.channel,"Backup Created")
    await client.send_message(message.channel,"Shutting down...")
    exit()


def main():
    if os.path.isfile('user_dictionary.txt'): # If a backup of the user dictionary exists, load it
        loadBackup(open('user_dictionary.txt','r'))
    
    client.run(token) # Log the bot into discord and run


if __name__ == '__main__': # If run as the main program
    main()
