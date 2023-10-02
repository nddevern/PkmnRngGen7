from __future__ import annotations
import Enums

class Type:
    def __init__(self, typeName: Enums.TypeName, weaknesses: list[Enums.TypeName], resistances: list[Enums.TypeName], immunities: list[Enums.TypeName]=[]):
        self.TypeName = typeName.name
        self.Weaknesses = weaknesses# list of TypeName
        self.Resistances = resistances# list of TypeName
        self.Immunities = immunities# list of TypeName
    
    # THE REST OF THIS FILE DEDICATED TO THE /WEAK COMMAND
    def GetTypesToPrint(self, outputDict: dict, listToPrint: list[Enums.TypeName], firstExcludedList: list[Enums.TypeName], secondExcludedList: list[Enums.TypeName]) -> dict:
        outputDict = self.GetListToPrint(outputDict, listToPrint)
        outputDict = self.ExcludeTypesFromList(outputDict, firstExcludedList)
        outputDict = self.ExcludeTypesFromList(outputDict, secondExcludedList)
        return outputDict
    
    def GetListToPrint(self, outputDict: dict, typesToGet: list[Enums.TypeName]) -> dict:
        for type in typesToGet:
            weaknessLevel = outputDict.get(type.value, 0)
            weaknessLevel += 1
            outputDict[type.value] = weaknessLevel
        return outputDict
    
    def ExcludeTypesFromList(self, outputDict: dict, typesToExclude: list[Enums.TypeName]) -> dict:
        for type in typesToExclude:
            if type.value in outputDict:
                outputDict.pop(type.value)
        return outputDict