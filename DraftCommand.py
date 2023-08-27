from __future__ import annotations
import Pokemon
import Player
import CommonFunctions
import PokemonDict
import InputHandling
import TypeDict
import Enums
import math

# return true if successful
def ExecuteDraftCommand(pokemonDict: PokemonDict.PokemonDict, typeDict: TypeDict.TypeDict) -> bool:
    print("BEGINNING DRAFT.")
    players = GetPlayers()

    # This is the array of pokemon who have not yet been chosen
    availablePokemon = GeneratePokemon(pokemonDict, len(players))

    #main draft loop
    longestPokemonNameLength = pokemonDict.GetLongestPokemonNameLength()
    currentPlayerIndex = 0
    currentPlayerIndexVelocity = 1
    draftedPokemon = 0
    while (draftedPokemon < 6*len(players)):
        # PRINT PLAYER INFO
        PrintDraftPlayerList(players, longestPokemonNameLength, currentPlayerIndex)

        # PRINT POKEMON INFO
        PrintUndraftedPokemonList(availablePokemon, longestPokemonNameLength)

        # HANDLE CHOOSING A POKEMON
        selectedIndex = InputHandling.GetInt("Please enter the number of the Pokemon you'd like to draft:", confirm=True, enforcedMinimum=1, enforcedMaximum=len(availablePokemon))-1
        players[currentPlayerIndex].AddPokemon(availablePokemon.pop(selectedIndex))
        currentPlayerIndex += currentPlayerIndexVelocity
        if currentPlayerIndex >= len(players):
            currentPlayerIndex = len(players)-1
            currentPlayerIndexVelocity = -1
        elif currentPlayerIndex < 0:
            currentPlayerIndex = 0
            currentPlayerIndexVelocity = 1
        draftedPokemon += 1
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    print("ALL POKEMON DRAFTED:")
    PrintDraftPlayerList(players, longestPokemonNameLength, -2)

    InputHandling.GetYesOrNo("Please confirm when all players have completed teambuilding")
    InputHandling.GetYesOrNo("You're sure of this?")

    # todo implement randomization of game play order

    return True

def GetPlayers() -> list[Player.Player]:
    playerCount = InputHandling.GetInt("How many players?", maxSaneValue=10, enforcedMinimum=1)
    players = []
    for i in range(playerCount):
        playerName = InputHandling.GetString("Please enter the name of player " + str(i+1) + ":", maxLength=20)
        newPlayer = Player.Player(playerName)
        players.append(newPlayer)

    players = CommonFunctions.ShuffleList(players)
    for i in range(playerCount):
        players[i].TurnOrder = i
    return players

def GeneratePokemon(pokemonDict: PokemonDict.PokemonDict, playerCount: int) -> list[Pokemon.Pokemon]:
    pokemonPerPlayer = InputHandling.GetInt("How many pokemon per player? (We usually do 12)", maxSaneValue=40, enforcedMinimum=1)
    numPokemonToGenerate = pokemonPerPlayer * playerCount
    print("Generating " + str(numPokemonToGenerate) + " pokemon...\n")

    availablePokemon = []
    for i in range(numPokemonToGenerate):
        availablePokemon.append(pokemonDict.GetRandom())
    availablePokemon = SortAvailablePokemonByTierThenByName(availablePokemon)
    return availablePokemon

# Thanks to Mohit Kumra: https://www.geeksforgeeks.org/insertion-sort/
def SortAvailablePokemonByTierThenByName(availablePokemon: list[Pokemon.Pokemon]) -> list[Pokemon.Pokemon]:
    for i in range(1, len(availablePokemon)):
        temp = availablePokemon[i]
        j = i-1
        while j >= 0 and (temp.Tier < availablePokemon[j].Tier or (temp.Tier == availablePokemon[j].Tier and temp.GetName() < availablePokemon[j].GetName())):
            availablePokemon[j+1] = availablePokemon[j]
            j -= 1
        availablePokemon[j + 1] = temp
    
    return availablePokemon

def GetLongestPlayerName(players: list[Player.Player]) -> int:
    longestPlayerNameLength = 0
    for i in range(len(players)):
        currentNameLength = len(players[i].Name)
        if currentNameLength > longestPlayerNameLength:
            longestPlayerNameLength = currentNameLength
    return longestPlayerNameLength

# desired format:
#
#       /- Length (dashes): max(longestPlayerName, longestPokemonNameInTheGame+2)+2
#       |
#       |                                                                     It's this player's turn.
# |-----+--------|                                                            |
#                                                                             v
# +--------------+--------------+--------------+--------------+--------------+==============+--------------+--------------+
# | Noah         | Noah         | Noah         | Noah         | Noah         > Noah         < Noah         | Noah         |
# | - Blastoise  | - Blastoise  | - Blastoise  | - Blastoise  | - Blastoise  ( - Blastoise  ) - Blastoise  | - Blastoise  |
# | - Charmander | - Charmander | - Charmander | - Charmander | - Charmander ( - Charmander ) - Charmander | - Charmander |
# | - Xerneas    | - Xerneas    | - Xerneas    | - Xerneas    | - Xerneas    ( - Xerneas    ) - Xerneas    | - Xerneas    |
# | - Beedrill   | - Beedrill   | - Beedrill   | - Beedrill   | - Beedrill   ( - Beedrill   ) - Beedrill   | - Beedrill   |
# | - Caterpie   | - Caterpie   | - Caterpie   | - Caterpie   | - Caterpie   ( - Caterpie   ) - Caterpie   | - Caterpie   |
# | - Palkia     | - Palkia     | - Palkia     | - Palkia     | - Palkia     ( - Palkia     ) - Palkia     | - Palkia     |
# +--------------+--------------+--------------+--------------+--------------+==============+--------------+--------------+

# currentTurnIndex is essentially an index into players where it is currently players[i]'s turn to pick a pokemon.
def PrintDraftPlayerList(players: list[Player.Player], longestPokemonNameLength: int, currentTurnIndex: int):
    playerInnerBoxWidth = max(GetLongestPlayerName(players), longestPokemonNameLength+2)+2
    numPlayers = len(players)

    printString = ""
    # header
    printString += PrintPlayerListHeaderOrFooter(playerInnerBoxWidth, currentTurnIndex, numPlayers)
    
    #player names
    printString += PrintPlayerNames(players, playerInnerBoxWidth, currentTurnIndex, numPlayers)
    printString += PrintPlayerPokemon(players, playerInnerBoxWidth, currentTurnIndex, numPlayers)
    # footer
    printString += PrintPlayerListHeaderOrFooter(playerInnerBoxWidth, currentTurnIndex, numPlayers)
    
    print(printString)

def PrintPlayerListHeaderOrFooter(playerInnerBoxWidth: int, currentTurnIndex: int, numPlayers: int) -> str:
    retString = "+"
    for i in range(numPlayers):
        characterToFill = "-"
        if i == currentTurnIndex:
            characterToFill = "="
        for j in range(playerInnerBoxWidth):
            retString += characterToFill
        retString += "+"
    return retString + "\n"

def PrintPlayerNames(players: list[Player.Player], playerInnerBoxWidth: int, currentTurnIndex: int, numPlayers: int) -> str:
    retString = ""
    for i in range(numPlayers):
        if i == currentTurnIndex:
            retString += '>'
        elif i-1 == currentTurnIndex:
            retString += '<'
        else: 
            retString += '|'
        retString += " "
        retString += players[i].Name.ljust(playerInnerBoxWidth-1)
    
    if numPlayers-1 == currentTurnIndex:
        retString += '<'
    else: 
        retString += '|'
    retString += '\n'
    return retString

def PrintPlayerPokemon(players: list[Player.Player], playerInnerBoxWidth: int, currentTurnIndex: int, numPlayers: int) -> str:
    retString = ""

    for i in range(6):
        retString += PrintOnePokemonLine(players, playerInnerBoxWidth, currentTurnIndex, numPlayers, i)

    return retString

def PrintOnePokemonLine(players: list[Player.Player], playerInnerBoxWidth: int, currentTurnIndex: int, numPlayers: int, currentPlayerPokemonIndex: int) -> str:
    retString = ""
    
    for i in range(numPlayers):
        if i == currentTurnIndex:
            retString += '('
        elif i-1 == currentTurnIndex:
            retString += ')'
        else: 
            retString += '|'
        retString += " - "
        retString += GetPlayerPokemonName(players[i], currentPlayerPokemonIndex).ljust(playerInnerBoxWidth-3)
    
    if numPlayers-1 == currentTurnIndex:
        retString += ')'
    else: 
        retString += '|'
    retString += '\n'

    return retString

def GetPlayerPokemonName(player: Player.Player, playerPokemonIndex: int) -> str:
    if len(player.PokemonList) > playerPokemonIndex:
        return player.PokemonList[playerPokemonIndex].GetName()
    else: 
        return ""

# desired format:
# 4 columns (TBD)
# [1] Uber PokemonName [4] OU   PokemonName
def PrintUndraftedPokemonList(availablePokemon: list[Pokemon.Pokemon], longestPokemonNameLength: int):
    printedPokemon = 0
    i = 0
    while printedPokemon < len(availablePokemon):
        printedPokemon = PrintUndraftedPokemonRow(availablePokemon, longestPokemonNameLength, i, printedPokemon)
        i += 1
    print("")


def PrintUndraftedPokemonRow(availablePokemon: list[Pokemon.Pokemon], longestPokemonNameLength: int, currentRow: int, printedPokemon: int) -> int:
    printString = ""
    availablePokemonCount = len(availablePokemon)
    colSize = math.ceil(availablePokemonCount/4)

    # col 1
    pokemonPrintString = GetPokemonPrintString(availablePokemon, longestPokemonNameLength, currentRow)
    if not pokemonPrintString.isspace():
        printedPokemon += 1
    printString += pokemonPrintString

    # col 2
    pokemonPrintString = GetPokemonPrintString(availablePokemon, longestPokemonNameLength, colSize+currentRow)
    if not pokemonPrintString.isspace():
        printedPokemon += 1
    printString += pokemonPrintString

    # col 3
    pokemonPrintString = GetPokemonPrintString(availablePokemon, longestPokemonNameLength, 2*colSize+currentRow)
    if not pokemonPrintString.isspace():
        printedPokemon += 1
    printString += pokemonPrintString

    # col 4
    pokemonPrintString = GetPokemonPrintString(availablePokemon, longestPokemonNameLength, 3*colSize+currentRow)
    if not pokemonPrintString.isspace():
        printedPokemon += 1
    printString += pokemonPrintString
    print(printString)
    return printedPokemon

def GetPokemonPrintString(availablePokemon: list[Pokemon.Pokemon], longestPokemonNameLength: int, pokemonIndex: int) -> str:
    #extra spaces added to ljusts to avoid + " " + 
    digitsOfMaxIndex = len(str(len(availablePokemon)-1))#length of the string representation of the max index into available pokemon
    if pokemonIndex < len(availablePokemon):
        pokemon = availablePokemon[pokemonIndex]
        indexPart = "[" + str(pokemonIndex+1) + "]" 
        return indexPart.rjust(digitsOfMaxIndex+2) + " " + pokemon.Tier.name.ljust(5) + pokemon.GetName().ljust(longestPokemonNameLength+2)
    else:
        return "".ljust(longestPokemonNameLength+digitsOfMaxIndex+9)