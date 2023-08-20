from __future__ import annotations
import Pokemon

class Player:
    def __init__(self, name, turnOrder: int, pokemon: list[Pokemon.Pokemon]=[]):
        self.Name = name
        self.TurnOrder = turnOrder
        self.Pokemon = pokemon