from __future__ import annotations
import Pokemon
import Player
import CommonFunctions
import PokemonDict
import InputHandling
import TypeDict
import Enums
import math
import Type
import ConfigSettings

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
    while ((draftedPokemon < 6*len(players)) and (len(availablePokemon) > 0)):
        # PRINT PLAYER INFO
        PrintDraftPlayerList(players, longestPokemonNameLength, currentPlayerIndex)

        # PRINT POKEMON INFO
        PrintUndraftedPokemonList(availablePokemon, pokemonDict, longestPokemonNameLength)

        # HANDLE CHOOSING A POKEMON
        print("It's " + players[currentPlayerIndex].Name + "'s turn.")
        selectedIndex = InputHandling.GetInt("Please enter the number of the Pokemon you'd like to draft:", confirm=ConfigSettings.CONFIRM_POKEMON_PICKS, enforcedMinimum=1, enforcedMaximum=len(availablePokemon))-1
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

    teambuildingComplete = False
    while(not teambuildingComplete):
        if InputHandling.GetYesOrNo("Please confirm when all players have completed teambuilding"):
            if InputHandling.GetYesOrNo("You're sure of this?"):
                teambuildingComplete = True

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
    pokemonPerPlayer = ConfigSettings.DEFAULT_POKEMON_TO_GENERATE_PER_PLAYER
    if pokemonPerPlayer < 1:
        pokemonPerPlayer = InputHandling.GetInt("How many pokemon per player? (We usually do 12)", maxSaneValue=40, enforcedMinimum=1)
    numPokemonToGenerate = pokemonPerPlayer * playerCount
    print("Generating " + str(numPokemonToGenerate) + " pokemon...\n")

    availablePokemon = []
    for i in range(numPokemonToGenerate):
        availablePokemon.append(pokemonDict.GetRandom())
    availablePokemon = SortAvailablePokemonList(availablePokemon, pokemonDict)
    return availablePokemon

# Thanks to Mohit Kumra: https://www.geeksforgeeks.org/insertion-sort/
def SortAvailablePokemonList(availablePokemon: list[Pokemon.Pokemon], pokemonDict: PokemonDict.PokemonDict) -> list[Pokemon.Pokemon]:
    for i in range(1, len(availablePokemon)):
        temp = availablePokemon[i]
        j = i-1
        while (j >= 0 and ComparePokemon(temp, availablePokemon[j], pokemonDict) < 0):
            availablePokemon[j+1] = availablePokemon[j]
            j -= 1
        availablePokemon[j+1] = temp
    
    return availablePokemon

# returns -1 if pokemon1 < pokemon2, 
#          0 if pokemon1 = pokemon2,
#          1 if pokemon1 > pokemon2
# the sorting function sorts ascending, so return -1 if it should be earlier in the list.

# Our sort priority:
# 1. Max potential tier desc
# 2. Evolves Needed asc
# 3. Current tier desc
# 4. Alphabetical
def ComparePokemon(pokemon1: Pokemon.Pokemon, pokemon2: Pokemon.Pokemon, pokemonDict: PokemonDict.PokemonDict) -> int:
    pokemon1HighestTier = pokemon1.GetFinalForm(pokemonDict).GetMegaTierElseMyTier()
    pokemon2HighestTier = pokemon2.GetFinalForm(pokemonDict).GetMegaTierElseMyTier()

    if (pokemon1HighestTier < pokemon2HighestTier):
        return -1
    elif (pokemon1HighestTier > pokemon2HighestTier):
        return 1
    elif(pokemon1.GetEvolvesNeeded(pokemonDict) < pokemon2.GetEvolvesNeeded(pokemonDict)):
        return -1
    elif(pokemon1.GetEvolvesNeeded(pokemonDict) > pokemon2.GetEvolvesNeeded(pokemonDict)):
        return 1
    elif(pokemon1.Tier < pokemon2.Tier):
        return -1
    elif(pokemon1.Tier > pokemon2.Tier):
        return 1
    elif(pokemon1.GetName() < pokemon2.GetName()):
        return -1
    elif(pokemon1.GetName() > pokemon2.GetName()):
        return 1
    else:
        return 0

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
def PrintUndraftedPokemonList(availablePokemon: list[Pokemon.Pokemon], pokemonDict: PokemonDict.PokemonDict, longestPokemonNameLength: int):
    printedPokemon = 0
    i = 0
    while printedPokemon < len(availablePokemon):
        printedPokemon = PrintUndraftedPokemonRow(availablePokemon, pokemonDict, longestPokemonNameLength, i, printedPokemon)
        i += 1
    print("")


def PrintUndraftedPokemonRow(availablePokemon: list[Pokemon.Pokemon], pokemonDict: PokemonDict.PokemonDict, longestPokemonNameLength: int, currentRow: int, printedPokemon: int) -> int:
    printString = ""
    availablePokemonCount = len(availablePokemon)
    colSize = math.ceil(availablePokemonCount/ConfigSettings.NUM_COLUMNS)

    for i in range(ConfigSettings.NUM_COLUMNS):
        includeTrailingSpaces = True
        if (i == (ConfigSettings.NUM_COLUMNS-1)):
            includeTrailingSpaces = False
        pokemonPrintString = GetPokemonPrintString(availablePokemon, pokemonDict, longestPokemonNameLength, i*colSize+currentRow, includeTrailingSpaces)
        if not pokemonPrintString.isspace():
            printedPokemon += 1
        printString += pokemonPrintString    

    print(printString)
    return printedPokemon

def GetPokemonPrintString(availablePokemon: list[Pokemon.Pokemon], pokemonDict: PokemonDict.PokemonDict, longestPokemonNameLength: int, pokemonIndex: int, includeTrailingSpaces=True) -> str:
    #extra spaces added to ljusts to avoid + " " + 
    
    if pokemonIndex >= len(availablePokemon):
        return ""
    retString = ""
    pokemon = availablePokemon[pokemonIndex]

    # index part
    digitsOfMaxIndex = len(str(len(availablePokemon)))#length of the string representation of the max displayed number into available pokemon
    retString += ("[" + str(pokemonIndex+1) + "]").rjust(digitsOfMaxIndex+2) + "  "
    
    # pokemon types part
    if (ConfigSettings.DISPLAY_UNDRAFTED_POKEMON_TYPES):
        retString += GetTypePrintString(pokemon.Type1) + " "
        retString += GetTypePrintString(pokemon.Type2) + "  "

    # pokemon tier part
    retString += GetPotentialPokemonInfoString(pokemon, pokemonDict)

    # pokemon name part
    pokemonNameString = pokemon.GetName()
    if includeTrailingSpaces:
        pokemonNameString = pokemonNameString.ljust(longestPokemonNameLength+2) # this handles the gap between pokemon names, which is defined as 2 spaces.
    retString += pokemonNameString + "  "

    return retString

def GetPotentialPokemonInfoString(pokemon: Pokemon.Pokemon, pokemonDict: PokemonDict.PokemonDict) -> str:
    retString = ""
    
    # current tier
    retString += CommonFunctions.GetTierPrintString(pokemon.Tier).rjust(4)

    if (not ConfigSettings.DISPLAY_UNDRAFTED_POKEMON_EVOLUTION_INFO):
        return retString + "  "

    # if their current pokemon is max evolve and cannot mega, skip arrow/potential and draw spaces.
    if (not pokemon.CanMega and pokemon.EvolvesIntoPokemonId <= 0):
        return retString.rjust(14) + "  "

    # arrow
    #  numEvolvesNeeded
    pokemonEvolvesNeeded = pokemon.GetEvolvesNeeded(pokemonDict)
    evolvesNeededString = "-"
    if (pokemonEvolvesNeeded > 0):
        evolvesNeededString = str(pokemonEvolvesNeeded)
    
    #  canMega
    finalEvolution = pokemon.GetFinalForm(pokemonDict)
    canMegaString = "-"
    if (pokemon.CanMega or finalEvolution.CanMega):
        canMegaString = "*" # Handles the case where they can mega but their max potential pokemon cannot (see Glalie) or where mega does not increase their tier (Mewtwo)
    if (finalEvolution.CanMega and finalEvolution.MegaTier < finalEvolution.Tier):
        canMegaString = "M"
    if (finalEvolution.PokemonId == Enums.PokemonName.Groudon.value or finalEvolution.PokemonId == Enums.PokemonName.Kyogre.value):
        canMegaString = "P"
    retString += " -" + evolvesNeededString + canMegaString + "> "
    
    # max potential tier
    retString += CommonFunctions.GetTierPrintString(finalEvolution.GetMegaTierElseMyTier()).rjust(4)
    return retString + "  "

def GetTypePrintString(typeObj: Type.Type) -> str:
    if typeObj is None:
        return "   "
    type = typeObj.TypeName
    if type is None:
        return "   "
    elif type == Enums.TypeName.Normal.name:
        return "NOR"
    elif type == Enums.TypeName.Fire.name:
        return "FIR"
    elif type == Enums.TypeName.Water.name:
        return "WAT"
    elif type == Enums.TypeName.Electric.name:
        return "ELE"
    elif type == Enums.TypeName.Grass.name:
        return "GRA"
    elif type == Enums.TypeName.Ice.name:
        return "ICE"
    elif type == Enums.TypeName.Fighting.name:
        return "FIG"
    elif type == Enums.TypeName.Poison.name:
        return "POI"
    elif type == Enums.TypeName.Ground.name:
        return "GRO"
    elif type == Enums.TypeName.Flying.name:
        return "FLY"
    elif type == Enums.TypeName.Psychic.name:
        return "PSY"
    elif type == Enums.TypeName.Bug.name:
        return "BUG"
    elif type == Enums.TypeName.Rock.name:
        return "ROC"
    elif type == Enums.TypeName.Ghost.name:
        return "GHO"
    elif type == Enums.TypeName.Dragon.name:
        return "DRA"
    elif type == Enums.TypeName.Dark.name:
        return "DAR"
    elif type == Enums.TypeName.Steel.name:
        return "STE"
    elif type == Enums.TypeName.Fairy.name:
        return "FAI"
    else:
        return "   "
    