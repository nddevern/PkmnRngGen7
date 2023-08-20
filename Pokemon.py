from __future__ import annotations
from colorama import Fore
from colorama import Style
import Type
import Enums
import CommonFunctions
import Constants

# todo: maybe one day I could store my optimal builds in this script, then add a command called "/optimal <pkmnName>" that shows that list.
#       if I did that, I'd have to store the optimal move spread, item, EVs/IVs, ability in this object.

class Pokemon:
    def __init__(self, name, type1: Type.Type, type2: Type.Type, tier: Enums.Tier, evolvesNeeded, canMega):
        self.Name = name
        self.Type1 = type1
        self.Type2 = type2
        self.Tier = tier
        self.CanMega = canMega
        self.EvolvesNeeded = evolvesNeeded
    
    def GetAllDefensiveTypeMatchupsString(self) -> str:
        retString = str(Style.BRIGHT + self.Name + Style.RESET_ALL + " - " + self.Type1.TypeName)
        if not self.Type2 is None:
            retString += "/" + self.Type2.TypeName
        retString += Constants.WEAKNESS_COLOR + Style.BRIGHT + "\nWeaknesses" + Style.RESET_ALL + ": " + self.GetWeaknesses(Constants.WEAKNESS_COLOR)
        retString += Constants.RESISTANCE_COLOR + Style.BRIGHT + "\nResistances" + Style.RESET_ALL + ": " + self.GetResistances(Constants.RESISTANCE_COLOR)
        retString += Constants.IMMUNITY_COLOR + Style.BRIGHT + "\nImmunities" + Style.RESET_ALL + ": " + self.GetImmunities(Constants.IMMUNITY_COLOR)
        return retString
    
    def GetWeaknesses(self, doubleEffectColor: str) -> str:
        WeaknessesToPrint = dict()#typeValue -> weaknessMultiplier
        WeaknessesToPrint = self.Type1.GetTypesToPrint(WeaknessesToPrint, self.Type1.Weaknesses, self.Type1.Resistances, self.Type1.Immunities)
        
        if not self.Type2 is None:
            WeaknessesToPrint = self.Type2.GetTypesToPrint(WeaknessesToPrint, self.Type2.Weaknesses, self.Type2.Resistances, self.Type2.Immunities)
        
        return CommonFunctions.GetTypeListString(WeaknessesToPrint, doubleEffectColor)
    
    def GetResistances(self, doubleEffectColor: str) -> str:
        ResistancesToPrint = dict()#typeValue -> weaknessMultiplier
        ResistancesToPrint = self.Type1.GetTypesToPrint(ResistancesToPrint, self.Type1.Resistances, self.Type1.Weaknesses, self.Type1.Immunities)
        
        if not self.Type2 is None:
            ResistancesToPrint = self.Type2.GetTypesToPrint(ResistancesToPrint, self.Type2.Resistances, self.Type2.Weaknesses, self.Type2.Immunities)
        
        return CommonFunctions.GetTypeListString(ResistancesToPrint, doubleEffectColor)
    
    def GetImmunities(self, doubleEffectColor: str) -> str:
        ImmunitiesToPrint = dict()#typeValue -> weaknessMultiplier
        ImmunitiesToPrint = self.Type1.GetTypesToPrint(ImmunitiesToPrint, self.Type1.Immunities, self.Type1.Weaknesses, self.Type1.Resistances)
        
        if not self.Type2 is None:
            ImmunitiesToPrint = self.Type2.GetTypesToPrint(ImmunitiesToPrint, self.Type2.Immunities, self.Type2.Weaknesses, self.Type2.Resistances)
        
        return CommonFunctions.GetTypeListString(ImmunitiesToPrint, doubleEffectColor)