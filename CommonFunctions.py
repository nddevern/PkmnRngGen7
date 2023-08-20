from __future__ import annotations
from colorama import Fore
from colorama import Style
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
                retString += Style.BRIGHT + doubleEffectColor + Enums.TypeName(key).name + Style.RESET_ALL# + " (x" + str(value) + ")"
        
        if retString == "":
            retString = Fore.LIGHTBLACK_EX + "None" + Style.RESET_ALL

        return retString