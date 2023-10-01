from __future__ import annotations
import Type
import Enums
import CommonFunctions
import Constants
import PokemonDict

# todo: maybe one day I could store my optimal builds in this script, then add a command called "/optimal <pkmnName>" that shows that list.
#       if I did that, I'd have to store the optimal move spread, item, EVs/IVs, ability in this object.

# Note: These should NOT hold instance variables. Each pokemon has 1 instance and when a player drafts it they are given a reference to that.
#       Meaning two players could both have a reference to the same pokemon instance.
class Pokemon:
    def __init__(self, pokemonId, type1: Type.Type, type2: Type.Type, tier: Enums.Tier, evolvesIntoPokemonId, generation, canMega, megaTier: Enums.Tier):
        self.PokemonId = pokemonId
        self.Type1 = type1
        self.Type2 = type2
        self.Tier = tier
        self.CanMega = canMega
        self.EvolvesIntoPokemonId = evolvesIntoPokemonId
        self.Generation = generation
        self.MegaTier = megaTier
    
    def GetName(self) -> str:
        retString = Enums.PokemonName(self.PokemonId).name
        retString = retString.replace("_", "-")
        #pokemon-specific adjustments
        retString = retString.replace("NidoranFemale", "Nidoran-F")
        retString = retString.replace("NidoranMale", "Nidoran-M")
        retString = retString.replace("TypeNull", "Type: Null")
        retString = retString.replace("Tapu", "Tapu ")
        retString = retString.replace("MrMime", "Mr. Mime")
        retString = retString.replace("MimeJr", "Mime Jr.")
        retString = retString.replace("Farfetchd", "Farfetch'd")
        return retString
    
    def GetEvolvesNeeded(self, pokemonDict: PokemonDict.PokemonDict) -> int:
        currentPokemon = self
        evolvesNeeded = 0
        while(currentPokemon.EvolvesIntoPokemonId > 0):
            currentPokemon = pokemonDict.Get(currentPokemon.EvolvesIntoPokemonId)
            evolvesNeeded += 1
        return evolvesNeeded
    
    def GetFinalForm(self, pokemonDict: PokemonDict.PokemonDict) -> Pokemon.Pokemon:
        currentPokemon = self
        while(currentPokemon.EvolvesIntoPokemonId > 0):
            currentPokemon = pokemonDict.Get(currentPokemon.EvolvesIntoPokemonId)
        return currentPokemon
    
    def GetMegaTierElseMyTier(self) -> Enums.Tier:
        if (self.CanMega):
            return self.MegaTier
        else:
            return self.Tier
    
    # debug
    def __str__(self) -> str:
        return "<Pokemon Name=" + self.GetName() + " Tier=" + self.Tier.name + ">"
    
    # THE REST OF THIS FILE IS ALL DEDICATED TO THE /WEAK COMMAND
    def GetAllDefensiveTypeMatchupsString(self) -> str:
        retString = str(Constants.STYLE_BRIGHT + self.GetName() + Constants.STYLE_RESET + " - " + self.Type1.TypeName)
        if not self.Type2 is None:
            retString += "/" + self.Type2.TypeName
        retString += Constants.COLOR_WEAKNESS + Constants.STYLE_BRIGHT + "\nWeaknesses" + Constants.STYLE_RESET + ": " + self.GetWeaknesses(Constants.COLOR_WEAKNESS)
        retString += Constants.COLOR_RESISTANCE + Constants.STYLE_BRIGHT + "\nResistances" + Constants.STYLE_RESET + ": " + self.GetResistances(Constants.COLOR_RESISTANCE)
        retString += Constants.COLOR_IMMUNITY + Constants.STYLE_BRIGHT + "\nImmunities" + Constants.STYLE_RESET + ": " + self.GetImmunities(Constants.COLOR_IMMUNITY)
        return retString
    
    def GetWeaknesses(self, doubleEffectColor: str) -> str:
        WeaknessesToPrint = dict()#typeValue -> weaknessMultiplier
        WeaknessesToPrint = self.Type1.GetTypesToPrint(WeaknessesToPrint, self.Type1.Weaknesses, [], [])
        
        if not self.Type2 is None:
            WeaknessesToPrint = self.Type2.GetTypesToPrint(WeaknessesToPrint, self.Type2.Weaknesses, self.Type2.Resistances, self.Type2.Immunities)
            WeaknessesToPrint = self.Type1.ExcludeTypesFromList(WeaknessesToPrint, self.Type1.Resistances)
            WeaknessesToPrint = self.Type1.ExcludeTypesFromList(WeaknessesToPrint, self.Type1.Immunities)
        
        return CommonFunctions.GetTypeListString(WeaknessesToPrint, doubleEffectColor)
    
    def GetResistances(self, doubleEffectColor: str) -> str:
        ResistancesToPrint = dict()#typeValue -> weaknessMultiplier
        ResistancesToPrint = self.Type1.GetTypesToPrint(ResistancesToPrint, self.Type1.Resistances, [], [])
        
        if not self.Type2 is None:
            ResistancesToPrint = self.Type2.GetTypesToPrint(ResistancesToPrint, self.Type2.Resistances, self.Type2.Weaknesses, self.Type2.Immunities)
            ResistancesToPrint = self.Type1.ExcludeTypesFromList(ResistancesToPrint, self.Type1.Weaknesses)
            ResistancesToPrint = self.Type1.ExcludeTypesFromList(ResistancesToPrint, self.Type1.Immunities)
        
        return CommonFunctions.GetTypeListString(ResistancesToPrint, doubleEffectColor)
    
    #"double immunities" are not handled by this function but they do not exist anyway
    def GetImmunities(self, doubleEffectColor: str) -> str:
        ImmunitiesToPrint = dict()#typeValue -> weaknessMultiplier
        ImmunitiesToPrint = self.Type1.GetTypesToPrint(ImmunitiesToPrint, self.Type1.Immunities, [], [])
        
        if not self.Type2 is None:
            ImmunitiesToPrint = self.Type2.GetTypesToPrint(ImmunitiesToPrint, self.Type2.Immunities, [], [])
        
        return CommonFunctions.GetTypeListString(ImmunitiesToPrint, doubleEffectColor)