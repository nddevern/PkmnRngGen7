from __future__ import annotations
import Constants
import Enums
import random
import Pokemon

def GetTypeListString(typeDict: dict, doubleEffectColor: str) -> str:
        retString = ""
        alreadyPrintedFirstItem = False
        for key, value in typeDict.items():
            if alreadyPrintedFirstItem:
                retString += ", "
            alreadyPrintedFirstItem = True

            if value == 1:
                retString += Enums.TypeName(key).name
            else:
                retString += Constants.STYLE_BRIGHT + doubleEffectColor + Enums.TypeName(key).name + Constants.STYLE_RESET + " (x" + str(value) + ")"
        
        if retString == "":
            retString = Constants.COLOR_NONE + "None" + Constants.STYLE_RESET

        return retString

# This algorithm uses the Fisher-Yates shuffle. See https://bost.ocks.org/mike/shuffle/ for more info.
def ShuffleList(list: list) -> list:
    size = len(list)
    for i in range(size):
        randomIndex = random.randint(i, size-1)
        temp = list[i]
        list[i] = list[randomIndex]
        list[randomIndex] = temp
    return list

def PrintList(list: list):
    retString = "["
    isFirstEntry = True
    for i in range(len(list)):
        if (not isFirstEntry):
            retString += ", "
        retString += list[i].__str__()
        isFirstEntry = False
    print(retString + "]")

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