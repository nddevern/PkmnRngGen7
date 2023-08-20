from __future__ import annotations
import Type
import Enums
import TypeDict
from Pokemon import Pokemon

# this is a wrapper class for a dictionary that contains Pokemon objects.
# key: string (pokemonName. TODO change this to the pokemon name enum if I make one).
# value: The Pokemon object.

class PokemonDict:
    def __init__(self):
        self.Dict = dict()

    def Add(self, pokemonName: str, type1: Type.Type, type2: Type.Type, tier: Enums.Tier, evolvesNeeded, generation, canMega=False):
        self.Dict[pokemonName] = Pokemon(pokemonName, type1, type2, tier, evolvesNeeded, generation, canMega)
    
    def Get(self, pokemonName: str) -> Pokemon:
        return self.Dict[pokemonName]
    
    def FillDict(self, types: TypeDict.TypeDict):
        #        PokemonName, type1, type2, tier, evolvesNeeded, canMega(default False) 
        #TEST DATA
        self.Add("TestGrassIceMon", types.Grass, types.Ice, Enums.Tier.OU, 0, 1, True)
        self.Add("TestGrassMon", types.Fairy, types.Steel, Enums.Tier.OU, 2, 0)
        self.Add("TestIceMon", types.Steel, types.Fairy, Enums.Tier.OU, 0, 3, True)