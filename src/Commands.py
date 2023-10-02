import Enums
import DraftCommand
import PokemonDict
import TypeDict

# TODO disable allowing command input in other input handlers. it is messy. they should only be able to enter a command if one is not already in progress.
class CommandHandler:
    def __init__(self, pokemonDict: PokemonDict.PokemonDict, typeDict: TypeDict.TypeDict):
        self.PokemonDict = pokemonDict
        self.TypeDict = typeDict

    # assumes string has been sanitized. returns true if success
    # TODO: allow arguments. The weak command currently is not functional due to not allowing arguments.
    def ExecuteCommand(self, string: str) -> bool:
        if string == Enums.Commands.DRAFT.value:
            # this command has its own file due to complicated code
            return DraftCommand.ExecuteDraftCommand(self.PokemonDict, self.TypeDict)
        if string == Enums.Commands.EXIT.value:
            return False
        if string == Enums.Commands.QUIT.value:
            return False
        if string == Enums.Commands.WEAK.value:
            return ExecuteWeakCommand(self.PokemonDict)
        return False

def ExecuteWeakCommand(pokemonDict: PokemonDict.PokemonDict):
    print(pokemonDict.Get(Enums.PokemonName.Bulbasaur.value).GetAllDefensiveTypeMatchupsString() + "\n")