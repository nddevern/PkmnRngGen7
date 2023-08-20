# TODO.
# this is intended to be a file which contains functions to handle user input.

# Runs a loop with the input() function that validates that an integer was entered.
# If the user enters a valid command instead, that is also allowed; this function executes the command and then continues to loop until a valid input is received.
# todo: also put this in a try catch so it can keep looping if an error happens.
# def GetInt(prompt: str, allowOtherCommands=True) -> int:
#   while(1):
#     pcInput = input(prompt)
#     sanitizedInput = SanitizeInput(pcInput)
#     if ValidInt(sanitizedInput):
#         # return the int
#     elif ValidCommand(sanitizedInput):
#         # run the command and loop
#     else:
#         # print a message telling the user that the input is not valid and loop (MAKE THIS MESSAGE GENERIC)

# just like GetInt, but for strings. used for getting user names.
# def GetString(prompt: str, allowOtherCommands=True) -> str:


# Returns a string with leading/trailing whitespace trimmed and with any other necessary sanitization performed.
# def SanitizeInput(input: str) -> str:

# returns true if the input is a valid integer, false otherwise.
# def ValidInt(input: str) -> bool:

# returns true if the input is a valid command matching a known command.
# reference for a list of several showdown commands: https://www.reddit.com/r/stunfisk/comments/du77on/showdown_useful_commands_list/
# def ValidCommand(input: str) -> bool:
