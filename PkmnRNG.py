from __future__ import annotations
import random
import math
import sys
from enum import IntEnum
import Type
import Pokemon
import Enums
import Player
import CommonFunctions
import TypeDict
import PokemonDict
import InputHandling

'''
Created on Aug 19, 2023
@author: Nodever2
'''

'''##########################################
############ Beginning of config ############
##########################################'''

'''##########################################
############### End of config ###############
##########################################'''

#todo: re-format this project to have all other files in a package. see https://docs.python.org/3/tutorial/modules.html#packages
#                                                                   and https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory

#FUNCTIONS====================
def main():
    print("INITIALIZATION:")
    #colorama_init()
    print("  Building type data...")
    typeDict = TypeDict.TypeDict()

    print("  Building Pokemon data...")
    pokemonDict = PokemonDict.PokemonDict()# This is a dictionary so that pokemon weakness lookups are fast.
    pokemonDict.FillDict(typeDict)

    print("INITIALIZATION COMPLETE.\n\n")

    players = GetPlayers()
    CommonFunctions.PrintList(players)
    print("\n")
    # This is the array of pokemon who have not yet been chosen
    availablePokemon = GeneratePokemon(pokemonDict, len(players))
    CommonFunctions.PrintList(availablePokemon)
    

    input("Program complete. Press Enter to close...")
    sys.exit()

    # todo: to implement randomization of player battle order.
    # sources for how to do this:
    #  1) https://web.archive.org/web/20170325012457/https://msdn.microsoft.com/en-us/library/aa289166.aspx
    #  2) https://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n
    #  3) https://stackoverflow.com/questions/39238479/how-to-generate-all-set-combinations-in-a-random-order

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
    availablePokemon = CommonFunctions.SortAvailablePokemonByTierThenByName(availablePokemon)
    return availablePokemon

#SCRIPT====================
main()