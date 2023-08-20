from enum import IntEnum

# docs: https://docs.python.org/3/library/enum.html#programmatic-access-to-enumeration-members-and-their-attributes

# I think we are going to need an IntEnum for pokemon names. This would make selecting a random pokemon from PokemonDict trivial.
# Then PokemonDict will have a key that is the enum int and we can just call PokemonDict(randomInteger).
# while you're at it, make constants for the min pokemon index and max one.

class TypeName(IntEnum):
    INVALID = 0
    Normal = 1
    Fire = 2
    Water = 3
    Electric = 4
    Grass = 5
    Ice = 6
    Fighting = 7
    Poison = 8
    Ground = 9
    Flying = 10
    Psychic = 11
    Bug = 12
    Rock = 13
    Ghost = 14
    Dragon = 15
    Dark = 16
    Steel = 17
    Fairy = 18

class Tier(IntEnum):# Lower is better
    INVALID = 0
    AG = 1
    Uber = 2
    OU = 3
    BelowOU = 4
    UUBL = 5
    UU = 6
    RUBL = 7
    RU = 8
    NUBL = 9
    NU = 10
    PUBL = 11
    PU = 12
    BelowPU = 13
    NFE = 14
    LC = 15