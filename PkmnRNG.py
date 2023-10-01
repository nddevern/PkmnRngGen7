from __future__ import annotations
import sys
from enum import IntEnum
import TypeDict
import PokemonDict
import InputHandling
import Commands

'''
Created on Aug 19, 2023
@author: Nodever2
'''

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

    commandHandler = Commands.CommandHandler(pokemonDict, typeDict)

    print("INITIALIZATION COMPLETE.\n\n")
    commandResult = True
    while (commandResult == True):
        commandResult = InputHandling.ExecuteCommand("Please enter a command.\n", commandHandler)
    

    input("Program complete. Press Enter to close...")
    sys.exit()

    # todo: to implement randomization of player battle order.
    # sources for how to do this:
    #  1) https://web.archive.org/web/20170325012457/https://msdn.microsoft.com/en-us/library/aa289166.aspx
    #  2) https://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n
    #  3) https://stackoverflow.com/questions/39238479/how-to-generate-all-set-combinations-in-a-random-order

#SCRIPT====================
main()