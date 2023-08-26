from __future__ import annotations
import Pokemon
import Player
import CommonFunctions
import PokemonDict
import InputHandling
import TypeDict

# return true if successful
def ExecuteDraftCommand(pokemonDict: PokemonDict.PokemonDict, typeDict: TypeDict.TypeDict) -> bool:
    players = GetPlayers()
    CommonFunctions.PrintList(players)
    print("\n")
    # This is the array of pokemon who have not yet been chosen
    availablePokemon = GeneratePokemon(pokemonDict, len(players))
    CommonFunctions.PrintList(availablePokemon)

    #main draft loop
    currentPlayerIndex = 1
    #while(1):
    for i in range(1):
        PrintDraftPlayerList(players, pokemonDict.GetLongestPokemonNameLength(), currentPlayerIndex)

    return True

def GetPlayers() -> list[Player.Player]:
    playerCount = InputHandling.GetInt("How many players?", maxSaneValue=10, enforcedMinimum=1)
    players = []
    for i in range(playerCount):
        playerName = InputHandling.GetString("Please enter the name of player " + str(i+1) + ":")
        player = Player.Player(playerName)
        players.append(player)

    players = CommonFunctions.ShuffleList(players)
    for i in range(playerCount):
        players[i].TurnOrder = i
    return players

def GeneratePokemon(pokemonDict: PokemonDict.PokemonDict, playerCount: int) -> list[Pokemon.Pokemon]:
    pokemonPerPlayer = InputHandling.GetInt("How many pokemon per player? (We usually do 12)", maxSaneValue=40, enforcedMinimum=1)
    numPokemonToGenerate = pokemonPerPlayer * playerCount
    print("Generating " + str(numPokemonToGenerate) + " pokemon...")

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
def PrintDraftPlayerList(players: list[Player.Player], longestPokemonNameLength, currentPlayerIndex):
    playerInnerBoxWidth = max(GetLongestPlayerName(players), longestPokemonNameLength+2)+2
    numPlayers = len(players)

    printString = ""
    # header
    printString += PrintPlayerListHeaderOrFooter(playerInnerBoxWidth, currentPlayerIndex, numPlayers)
    
    #player names
    printString += PrintPlayerNames(players, playerInnerBoxWidth, currentPlayerIndex, numPlayers)

    # footer
    printString += PrintPlayerListHeaderOrFooter(playerInnerBoxWidth, currentPlayerIndex, numPlayers)
    
    
    print(printString)

    #print pokemon

    return

def PrintPlayerListHeaderOrFooter(playerInnerBoxWidth, currentPlayerIndex, numPlayers) -> str:
    retString = "+"
    for i in range(numPlayers):
        characterToFill = "-"
        if i == currentPlayerIndex:
            characterToFill = "="
        for j in range(playerInnerBoxWidth):
            retString += characterToFill
        retString += "+"
    retString += "\n"
    return retString

def PrintPlayerNames(players, playerInnerBoxWidth, currentPlayerIndex, numPlayers) -> str:
    retString = ""
    for i in range(numPlayers):
        if i == currentPlayerIndex:
            retString += '>'
        elif i-1 == currentPlayerIndex:
            retString += '<'
        else: 
            retString += '|'
        retString += " "
        retString += players[i].Name.ljust(playerInnerBoxWidth-1)
    
    if numPlayers-1 == currentPlayerIndex:
        retString += '<'
    else: 
        retString += '|'
    retString += '\n'
    return retString