from __future__ import annotations
import Constants
import Enums

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
                retString += Constants.STYLE_BRIGHT + doubleEffectColor + Enums.TypeName(key).name + Constants.STYLE_RESET# + " (x" + str(value) + ")"
        
        if retString == "":
            retString = Constants.COLOR_NONE + "None" + Constants.STYLE_RESET

        return retString