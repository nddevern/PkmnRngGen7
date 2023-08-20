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

from asyncio.windows_events import NULL
import random
import math
import sys
from enum import Enum

class TypeName(Enum):
    INVALID = 0
    Normal = 1
    Fire = 2
    Water = 3
    Electric = 4
    Grass = 5
    Ice = 6
    Fighting = 7
    Poison = 8
    Ground = 9
    Flying = 10
    Psychic = 11
    Bug = 12
    Rock = 13
    Ghost = 14
    Dragon = 15
    Dark = 16
    Steel = 17
    Fairy = 18

class Tier(Enum):# Lower is better
    INVALID = 0
    AG = 1
    Uber = 2
    OU = 3
    BelowOU = 4
    UUBL = 5
    UU = 6
    RUBL = 7
    RU = 8
    NUBL = 9
    NU = 10
    PUBL = 11
    PU = 12
    BelowPU = 13
    NFE = 14
    LC = 15

class Type:
    def __init__(self, typeName: TypeName, weaknesses: list, resistances: list, immunities: list):
        self.TypeName = typeName.name
        self.Weaknesses = weaknesses#list of TypeName
        self.Resistances = resistances#list of TypeName
        self.Immunities = immunities#list of TypeName
    
    def GetWeaknessesToPrint(self, WeaknessesToPrint: dict):
        for weakness in self.Weaknesses:
            weaknessLevel = WeaknessesToPrint.get(weakness.value, 0)
            weaknessLevel += 1
            WeaknessesToPrint[weakness.value] = weaknessLevel
        
        for resistance in self.Resistances:
            if resistance.value in WeaknessesToPrint:
                WeaknessesToPrint.pop(resistance.value)

        return WeaknessesToPrint

class Pokemon:
    def __init__(self, name, type1: Type, type2: Type, tier: Tier, canMega):
        self.Name = name
        self.Type1 = type1
        self.Type2 = type2
        self.Tier = tier
        self.CanMega = canMega
    
    def GetWeaknesses(self):
        WeaknessesToPrint = dict()#typeValue -> weaknessMultiplier
        WeaknessesToPrint = self.Type1.GetWeaknessesToPrint(WeaknessesToPrint)
        
        if not self.Type2 is None:
            WeaknessesToPrint = self.Type2.GetWeaknessesToPrint(WeaknessesToPrint)

        retString = ""
        firstPrintedItem = True
        for key, value in WeaknessesToPrint.items():
            if not firstPrintedItem:
                retString = retString + ", "
            firstPrintedItem = False

            if value == 1:
                retString = retString + TypeName(key).name
            else:
                retString = TypeName(key).name + " (x" + value + ")"

        return retString

def AddPkmn(dict: dict, pokemonName: str, type1: Type, type2: Type, tier: Tier, canMega):
    dict[pokemonName] = Pokemon(pokemonName, type1, type2, tier, canMega)

def main():
    print("INITIALIZATION:")
    print("  Building type data...")
    #name, weaknessList, resistancesList, immunitiesList
    NormalType   = Type(TypeName.Normal, [TypeName.Fighting], [], [TypeName.Ghost])
    FireType     = Type(TypeName.Fire, [TypeName.Water, TypeName.Ground, TypeName.Rock], [TypeName.Fire, TypeName.Grass, TypeName.Ice, TypeName.Bug, TypeName.Steel, TypeName.Fairy], [])
    WaterType    = Type(TypeName.Water, [TypeName.Electric, TypeName.Grass], [TypeName.Fire, TypeName.Water, TypeName.Ice, TypeName.Steel], [])
    ElectricType = Type(TypeName.Electric, [TypeName.Ground], [TypeName.Electric, TypeName.Flying, TypeName.Steel])

    print("  Building Pokemon data...")
    Pokemon = dict()# This is a dictionary so that pokemon weakness lookups are fast.
    AddPkmn(Pokemon, "TestMon", NormalType, None, Tier.OU, True)
    
    print("Initialization complete.\n\n")
    print(str(Pokemon))
    print(str(Pokemon.get("TestMon")))
    print(Pokemon["TestMon"].GetWeaknesses())


    sys.exit()


main()