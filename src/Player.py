from __future__ import annotations
import Pokemon

class Player:
    def __init__(self, name, turnOrder: int=-1):
        self.Name = name
        self.TurnOrder = turnOrder
        self.PokemonList = list()
    
    def __str__(self) -> str:
        return "<Player: " + self.Name + ">"
    
    def AddPokemon(self, pokemon: Pokemon.Pokemon):
        self.PokemonList.append(pokemon)