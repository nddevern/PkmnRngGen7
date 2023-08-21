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
    types = TypeDict.TypeDict()

    print("  Building Pokemon data...")
    pokemon = PokemonDict.PokemonDict()# This is a dictionary so that pokemon weakness lookups are fast.
    pokemon.FillDict(types)

    print("INITIALIZATION COMPLETE.\n\n")
    print(pokemon.Get(Enums.PokemonName.Bulbasaur.value).GetAllDefensiveTypeMatchupsString() + "\n")
    #print(pokemon.Get("TestGrassMon").GetAllDefensiveTypeMatchupsString() + "\n")
    #print(pokemon.Get("TestIceMon").GetAllDefensiveTypeMatchupsString() + "\n")

    input("Press Enter to close...")
    sys.exit()

    # todo: to implement randomization of player battle order.
    # sources for how to do this:
    #  1) https://web.archive.org/web/20170325012457/https://msdn.microsoft.com/en-us/library/aa289166.aspx
    #  2) https://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n
    #  3) https://stackoverflow.com/questions/39238479/how-to-generate-all-set-combinations-in-a-random-order

#SCRIPT====================
main()