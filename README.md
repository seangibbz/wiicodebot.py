# wiicodebot
NOTE: This project has halted development in favour of Seriel 💖’s sleeker Ruby-based RiiConnect24 bot

This is a Discord bot written in Python (based on [discord.py](https://github.com/Rapptz/discord.py) "discord.py") meant for the RiiConnect24 chatroom.

It handles user data regarding wii friend codes

## Done:
* Set a user's FC for a specific game
* Display a list of supported games for the database
* Display a list of all users with at least one registered FC
* Display a list of users who have registered a FC for a specific game
* Display friend code for a specific user for a specific game
* Display all users and friend codes for a specific game
* Backing up the database in the event of a dev using the `terminate()` method
* Loading backup files if restarting the bot after using the `terminate()` method
* Making commands not case-sensitive (i.e. so that `!getallgames` will run the same as `!getAllGames`)
* Make getCode function disregard the “@“ symbol at the start of mentions when searching for users
* Create a separate !backup command for the devs to use, that’s not dependent on !terminate. That way they can make backups of the database without having to kill the bot
* A `getUsersOf` method to return a list of users who play a specific game
* A `getUsersAndCodesOf` method to return a list of users and codes for a specific game
* A `getUserCodes` method to get all registered friend codes of a specific user

## To Do:
* `help()` method for providing users with easy documentation
* Setting up the `terminate()` method so it’ll only execute if the user is a dev
* Setting the script up on a cloud server so I don’t need to have my personal laptop on 24/7
* Option to delete games/codes from a user’s information
* Option for a user to delete their information entirely
* Checking that friend codes are entered in the right format (`####-####-####-####` for `WII1`/`WII2`/`WII3`, `####-####-####` for everything else) - will implement via regular expressions later
* Add optional additional argument in `!help` that will allow for explanation of specific commands (e.g. `!help setCode` will return documentation for `!setCode`)


## Credits
Sean Gibbons (seangibbz#5609 on Discord)

Danny (Rapptz) for discord.py