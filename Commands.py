import Enums
import DraftCommand
import PokemonDict
import TypeDict

class CommandHandler:
    def __init__(self, pokemonDict: PokemonDict.PokemonDict, typeDict: TypeDict.TypeDict):
        self.PokemonDict = pokemonDict
        self.TypeDict = typeDict

    # assumes string has been sanitized. returns true if success
    def ExecuteCommand(self, string: str) -> bool:
        if string == Enums.Commands.DRAFT.value:
            return DraftCommand.ExecuteDraftCommand(self.PokemonDict, self.TypeDict)
        return False