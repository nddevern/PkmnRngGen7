from __future__ import annotations
import random
import math
import sys
from enum import IntEnum
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

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

#ENUMS====================
class T(IntEnum):#THIS IS SUPPOSED TO BE CALLED TypeName BUT I AM RENAMING IT TO T WHILE I INSERT A TON OF DATA.
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

class Tier(IntEnum):# Lower is better
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

#CLASSES====================
class Type:
    def __init__(self, typeName: T, weaknesses: list[T], resistances: list[T], immunities: list[T]):
        self.TypeName = typeName.name
        self.Weaknesses = weaknesses#list of TypeName
        self.Resistances = resistances#list of TypeName
        self.Immunities = immunities#list of TypeName
    
    def GetTypesToPrint(self, outputDict: dict, listToPrint: list[T], firstExcludedList: list[T], secondExcludedList: list[T]):
        outputDict = self.GetListToPrint(outputDict, listToPrint)
        outputDict = self.ExcludeTypesFromList(outputDict, firstExcludedList)
        outputDict = self.ExcludeTypesFromList(outputDict, secondExcludedList)
        return outputDict
    
    def GetListToPrint(self, outputDict: dict, typesToGet: list[T]):
        for type in typesToGet:
            weaknessLevel = outputDict.get(type.value, 0)
            weaknessLevel += 1
            outputDict[type.value] = weaknessLevel
        return outputDict
    
    def ExcludeTypesFromList(self, outputDict: dict, typesToExclude: list[T]):
        for type in typesToExclude:
            if type.value in outputDict:
                outputDict.pop(type.value)
        return outputDict

class Pokemon:
    def __init__(self, name, type1: Type, type2: Type, tier: Tier, canMega, evolvesNeeded):
        self.Name = name
        self.Type1 = type1
        self.Type2 = type2
        self.Tier = tier
        self.CanMega = canMega
        self.EvolvesNeeded = evolvesNeeded
    
    def GetAllDefensiveTypeMatchupsString(self):
        retString = str(Style.BRIGHT + self.Name + Style.RESET_ALL + " - " + self.Type1.TypeName)
        if not self.Type2 is None:
            retString += "/" + self.Type2.TypeName
        retString += Fore.RED + Style.BRIGHT + "\nWeaknesses" + Style.RESET_ALL + ": " + self.GetWeaknesses(Fore.RED)
        retString += Fore.BLUE + Style.BRIGHT + "\nResistances" + Style.RESET_ALL + ": " + self.GetResistances(Fore.BLUE)
        retString += Fore.LIGHTBLACK_EX + Style.BRIGHT + "\nImmunities" + Style.RESET_ALL + ": " + self.GetImmunities(Fore.LIGHTBLACK_EX)
        return retString
    
    def GetWeaknesses(self, doubleEffectColor):
        WeaknessesToPrint = dict()#typeValue -> weaknessMultiplier
        WeaknessesToPrint = self.Type1.GetTypesToPrint(WeaknessesToPrint, self.Type1.Weaknesses, self.Type1.Resistances, self.Type1.Immunities)
        
        if not self.Type2 is None:
            WeaknessesToPrint = self.Type2.GetTypesToPrint(WeaknessesToPrint, self.Type2.Weaknesses, self.Type2.Resistances, self.Type2.Immunities)
        
        return self.GetTypeListString(WeaknessesToPrint, doubleEffectColor)
    
    def GetResistances(self, doubleEffectColor):
        ResistancesToPrint = dict()#typeValue -> weaknessMultiplier
        ResistancesToPrint = self.Type1.GetTypesToPrint(ResistancesToPrint, self.Type1.Resistances, self.Type1.Weaknesses, self.Type1.Immunities)
        
        if not self.Type2 is None:
            ResistancesToPrint = self.Type2.GetTypesToPrint(ResistancesToPrint, self.Type2.Resistances, self.Type2.Weaknesses, self.Type2.Immunities)
        
        return self.GetTypeListString(ResistancesToPrint, doubleEffectColor)
    
    def GetImmunities(self, doubleEffectColor):
        ImmunitiesToPrint = dict()#typeValue -> weaknessMultiplier
        ImmunitiesToPrint = self.Type1.GetTypesToPrint(ImmunitiesToPrint, self.Type1.Immunities, self.Type1.Weaknesses, self.Type1.Resistances)
        
        if not self.Type2 is None:
            ImmunitiesToPrint = self.Type2.GetTypesToPrint(ImmunitiesToPrint, self.Type2.Immunities, self.Type2.Weaknesses, self.Type2.Resistances)
        
        return self.GetTypeListString(ImmunitiesToPrint, doubleEffectColor)
    
    def GetTypeListString(self, typeDict: dict, doubleEffectColor):
        retString = ""
        alreadyPrintedFirstItem = False
        for key, value in typeDict.items():
            if alreadyPrintedFirstItem:
                retString += ", "
            alreadyPrintedFirstItem = True

            if value == 1:
                retString += T(key).name
            else:
                retString += Style.BRIGHT + doubleEffectColor + T(key).name + Style.RESET_ALL# + " (x" + str(value) + ")"
        
        if retString == "":
            retString = Fore.LIGHTBLACK_EX + "None" + Style.RESET_ALL

        return retString

#FUNCTIONS====================
def AddPkmn(dict: dict, pokemonName: str, type1: Type, type2: Type, tier: Tier, canMega, evolvesNeeded):
    dict[pokemonName] = Pokemon(pokemonName, type1, type2, tier, canMega, evolvesNeeded)

def main():
    print("INITIALIZATION:")
    colorama_init()
    print("  Building type data...")
    #name, weaknessList, resistancesList, immunitiesList
    NormalType   = Type(T.Normal, [T.Fighting], [], [T.Ghost])
    FireType     = Type(T.Fire, [T.Water, T.Ground, T.Rock], [T.Fire, T.Grass, T.Ice, T.Bug, T.Steel, T.Fairy], [])
    WaterType    = Type(T.Water, [T.Electric, T.Grass], [T.Fire, T.Water, T.Ice, T.Steel], [])
    ElectricType = Type(T.Electric, [T.Ground], [T.Electric, T.Flying, T.Steel], [])
    GrassType    = Type(T.Grass, [T.Fire, T.Ice, T.Poison, T.Flying, T.Bug], [T.Water, T.Electric, T.Grass, T.Ground], [])
    IceType      = Type(T.Ice, [T.Fire, T.Fighting, T.Rock, T.Steel], [T.Ice], [])
    FightingType = Type(T.Fighting, [T.Flying, T.Psychic, T.Fairy], [T.Bug, T.Rock, T.Dark], [])
    PoisonType   = Type(T.Poison, [T.Ground, T.Psychic], [T.Grass, T.Fighting, T.Poison, T.Bug, T.Fairy], [])
    GroundType   = Type(T.Ground, [T.Water, T.Grass, T.Ice], [T.Poison, T.Rock], [T.Electric])
    #todo finish

    print("  Building Pokemon data...")
    Pokemon = dict()# This is a dictionary so that pokemon weakness lookups are fast.
    #       list,     PokemonName, type1, type2, tier, canMega, evolvesNeeded 
    #TEST DATA
    AddPkmn(Pokemon, "TestGrassIceMon", GrassType, IceType, Tier.OU, True, 0)
    AddPkmn(Pokemon, "TestGrassMon", GrassType, None, Tier.OU, True, 0)
    AddPkmn(Pokemon, "TestIceMon", IceType, None, Tier.OU, True, 0)
    
    print("INITIALIZATION COMPLETE.\n\n")
    print(Pokemon["TestGrassIceMon"].GetAllDefensiveTypeMatchupsString() + "\n")
    print(Pokemon["TestGrassMon"].GetAllDefensiveTypeMatchupsString() + "\n")
    print(Pokemon["TestIceMon"].GetAllDefensiveTypeMatchupsString() + "\n")

    input("Press Enter to close...")
    sys.exit()

#SCRIPT====================
main()