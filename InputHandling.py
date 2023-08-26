import Commands

# this is a file which contains functions to handle user input.
# ALL NON-STRING INPUT IS SANITIZED INTO LOWER CASE!!!

# Performs string sanitization while also converting to lowercase for string comparisons on non-string input data
def SanitizeInput(input: str) -> str:
    return SanitizeStringInput(input).lower()

# Sanitizes string input without changing string contents
def SanitizeStringInput(input: str) -> str:
    return input.strip()

# Does not return until a valid integer has been input. Returns the int.
def GetInt(prompt: str, allowOtherCommands=True, confirm=False, maxSaneValue=99, enforcedMinimum=-999) -> int:
    while(1):
        printErrorMessageOnLoop = True
        try:
            pcInput = input(prompt + " ")
            sanitizedInput = SanitizeInput(pcInput)
            if ValidInt(sanitizedInput, enforcedMinimum=enforcedMinimum):
                finalInput = int(sanitizedInput)
                if finalInput > maxSaneValue:
                    if GetYesOrNo("High input value detected. Are you sure you meant " + str(finalInput) + "?"):
                        return finalInput
                    else: 
                        printErrorMessageOnLoop = False
                else:
                    return finalInput
            #elif ValidCommand(sanitizedInput) AND allowOtherCommands:
            # # run the command and loop
            if printErrorMessageOnLoop:
                print("Expected an integer input. Please try again.")
        except Exception:
            print("An error occurred. Please try again.")

# returns true if the input is a valid integer, false otherwise.
def ValidInt(input: str, enforcedMinimum) -> bool:
    try:
        if not input.isalnum():
            return False
        returnedValue = int(input)
        if returnedValue < enforcedMinimum:
            return False
        return True
    except ValueError:
        return False

# Does not return until a valid Yes/No has been input. Returns a bool of the result.
def GetYesOrNo(prompt: str, allowOtherCommands=False, confirm=False) -> bool:
    while(1):
        printErrorMessageOnLoop = True
        try:
            pcInput = input(prompt + " (Y/N) ")
            sanitizedInput = SanitizeInput(pcInput)
            if ValidYesNo(sanitizedInput):
                if IsYes(sanitizedInput):
                    return True
                elif IsNo(sanitizedInput):
                    return False
            #elif ValiCommand: execute the command.
            if printErrorMessageOnLoop:
                print("Expected Yes or No input. Please try again.")
        except Exception:
            print("An error occurred. Please try again.")

def ValidYesNo(input: str) -> bool:
    try:
        if not input.isalpha():
            return False
        if IsYes(input):
            return True
        if IsNo(input):
            return True
        return False
    except Exception:
        return False

def IsYes(input: str) -> bool:
    try:
        if input == "yes":
            return True
        elif input == "y":
            return True
        elif input == "y":
            return True
        elif input == "true":
            return True
        else:
            return False
    except Exception:
        return False

def IsNo(input: str) -> bool:
    try:
        if input == "no":
            return True
        elif input == "n":
            return True
        elif input == "f":
            return True
        elif input == "false":
            return True
        else:
            return False
    except Exception:
        return False

# Does not return until a valid string has been input. Returns the string.
def GetString(prompt: str, allowOtherCommands=True) -> str:
    while(1):
        printErrorMessageOnLoop = True
        try:
            pcInput = input(prompt + " ")
            sanitizedInput = SanitizeStringInput(pcInput)
            if ValidStringInput(sanitizedInput):
                return sanitizedInput
            #elif ValidComand: execute the command.
            if printErrorMessageOnLoop:
                print("Expected string input. How did you even mess this up? Please try again.")
        except Exception:
            print("An error occurred. Please try again.")

def ValidStringInput(input: str) -> bool:
    try:
        if not input.isascii():
            return False
        if input.isspace():
            return False
        return True
    except Exception:
        return False

def ExecuteCommand(prompt: str, commandHandler: Commands.CommandHandler):
    while(1):
        printErrorMessageOnLoop = True
        try:
            pcInput = input(prompt + " ")
            sanitizedInput = SanitizeStringInput(pcInput)
            if ValidStringInput(sanitizedInput):
                success = commandHandler.ExecuteCommand(sanitizedInput)
                if success:
                    return
            if printErrorMessageOnLoop:
                print("Expected command input. Please try again.")
        except Exception as e:
            print("An error occurred: " + str(e) + ". Please try again.")

# returns true if the input is a valid command matching a known command.
# reference for a list of several showdown commands: https://www.reddit.com/r/stunfisk/comments/du77on/showdown_useful_commands_list/
# def ValidCommand(input: str) -> bool:


# /weak command: print(pokemon.Get(Enums.PokemonName.Bulbasaur.value).GetAllDefensiveTypeMatchupsString() + "\n")