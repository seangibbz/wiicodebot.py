# wiicodebot
This is a Discord bot written in Python meant for the RiiConnect24 chatroom.
It handles user data regarding wii friend codes

## Done:
1. Set a user's FC for a specific game
2. Display a list of supported games for the database
3. Display a list of all users with at least one registered FC
4. Display a list of users who have registered a FC for a specific game
5. Display friend code for a specific user for a specific game
6. Display all users and friend codes for a specific game
7. Backing up the database in the event of a dev using the `terminate()` method

## To Do:
8. `help()` method for providing users with easy documentation
9. Loading backup files if restarting the bot after using the `terminate()` method
10. Making commands not case-sensitive (i.e. so that `!getallgames` will run the same as `!getAllGames`)
11. Setting up the `terminate()` method so it’ll only execute if the user is a dev
12. Setting the script up on a cloud server so I don’t need to have my personal laptop on 24/7
13. Option to delete games/codes from a user’s information
14. Option for a user to delete their information entirely
15. Checking that friend codes are entered in the right format (`####-####-####-####` for `WII1`/`WII2`/`WII3`, `####-####-####` for everything else) - will implement via regular expressions later

## Credits
Sean Gibbons (seangibbz#5609 on Discord)