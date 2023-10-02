import Enums
from Type import Type

# this is a class that has a property for each type.
# those type properties are the full Type class which means they have a list of weaknesses,resistances,immunities and the helper functions associated with them.

class TypeDict:
    def __init__(self):

        #format:
        # TypeName,
        # List<TypeName> Weaknesses,
        # List<TypeName> Resistances,
        # Optional List<TypeName> Immunities = []

        self.Normal   = Type(
            Enums.TypeName.Normal,
            [Enums.TypeName.Fighting],
            [],
            [Enums.TypeName.Ghost]
        )
        self.Fire     = Type(
            Enums.TypeName.Fire,
            [Enums.TypeName.Water, Enums.TypeName.Ground, Enums.TypeName.Rock],
            [Enums.TypeName.Fire, Enums.TypeName.Grass, Enums.TypeName.Ice, Enums.TypeName.Bug, Enums.TypeName.Steel, Enums.TypeName.Fairy]
        )
        self.Water    = Type(
            Enums.TypeName.Water,
            [Enums.TypeName.Electric, Enums.TypeName.Grass],
            [Enums.TypeName.Fire, Enums.TypeName.Water, Enums.TypeName.Ice, Enums.TypeName.Steel]
        )
        self.Electric = Type(
            Enums.TypeName.Electric,
            [Enums.TypeName.Ground],
            [Enums.TypeName.Electric, Enums.TypeName.Flying, Enums.TypeName.Steel]
        )
        self.Grass    = Type(
            Enums.TypeName.Grass,
            [Enums.TypeName.Fire, Enums.TypeName.Ice, Enums.TypeName.Poison, Enums.TypeName.Flying, Enums.TypeName.Bug],
            [Enums.TypeName.Water, Enums.TypeName.Electric, Enums.TypeName.Grass, Enums.TypeName.Ground]
        )
        self.Ice      = Type(
            Enums.TypeName.Ice,
            [Enums.TypeName.Fire, Enums.TypeName.Fighting, Enums.TypeName.Rock, Enums.TypeName.Steel],
            [Enums.TypeName.Ice]
        )
        self.Fighting = Type(
            Enums.TypeName.Fighting,
            [Enums.TypeName.Flying, Enums.TypeName.Psychic, Enums.TypeName.Fairy],
            [Enums.TypeName.Bug, Enums.TypeName.Rock, Enums.TypeName.Dark]
        )
        self.Poison   = Type(
            Enums.TypeName.Poison,
            [Enums.TypeName.Ground, Enums.TypeName.Psychic],
            [Enums.TypeName.Grass, Enums.TypeName.Fighting, Enums.TypeName.Poison, Enums.TypeName.Bug, Enums.TypeName.Fairy]
        )
        self.Ground   = Type(
            Enums.TypeName.Ground,
            [Enums.TypeName.Water, Enums.TypeName.Grass, Enums.TypeName.Ice],
            [Enums.TypeName.Poison, Enums.TypeName.Rock],
            [Enums.TypeName.Electric]
        )
        self.Flying   = Type(
            Enums.TypeName.Flying,
            [Enums.TypeName.Electric, Enums.TypeName.Ice, Enums.TypeName.Rock],
            [Enums.TypeName.Grass, Enums.TypeName.Fighting, Enums.TypeName.Bug],
            [Enums.TypeName.Ground]
        )
        self.Psychic  = Type(
            Enums.TypeName.Psychic,
            [Enums.TypeName.Bug, Enums.TypeName.Ghost, Enums.TypeName.Dark],
            [Enums.TypeName.Fighting, Enums.TypeName.Psychic]
        )
        self.Bug      = Type(
            Enums.TypeName.Bug,
            [Enums.TypeName.Fire, Enums.TypeName.Flying, Enums.TypeName.Rock],
            [Enums.TypeName.Grass, Enums.TypeName.Fighting, Enums.TypeName.Ground]
        )
        self.Rock     = Type(
            Enums.TypeName.Rock,
            [Enums.TypeName.Water, Enums.TypeName.Grass, Enums.TypeName.Fighting, Enums.TypeName.Ground, Enums.TypeName.Steel],
            [Enums.TypeName.Normal, Enums.TypeName.Fire, Enums.TypeName.Poison, Enums.TypeName.Flying]
        )
        self.Ghost    = Type(
            Enums.TypeName.Ghost,
            [Enums.TypeName.Ghost, Enums.TypeName.Dark],
            [Enums.TypeName.Poison, Enums.TypeName.Bug],
            [Enums.TypeName.Normal, Enums.TypeName.Fighting]
        )
        self.Dragon   = Type(
            Enums.TypeName.Dragon,
            [Enums.TypeName.Ice, Enums.TypeName.Dragon, Enums.TypeName.Fairy],
            [Enums.TypeName.Fire, Enums.TypeName.Water, Enums.TypeName.Electric, Enums.TypeName.Grass]
        )
        self.Dark     = Type(
            Enums.TypeName.Dark,
            [Enums.TypeName.Fighting, Enums.TypeName.Bug, Enums.TypeName.Fairy],
            [Enums.TypeName.Ghost, Enums.TypeName.Dark],
            [Enums.TypeName.Psychic]
        )
        self.Steel    = Type(
            Enums.TypeName.Steel,
            [Enums.TypeName.Fire, Enums.TypeName.Fighting, Enums.TypeName.Ground],
            [Enums.TypeName.Normal, Enums.TypeName.Grass, Enums.TypeName.Ice, Enums.TypeName.Flying, Enums.TypeName.Psychic, Enums.TypeName.Bug, Enums.TypeName.Rock, Enums.TypeName.Dragon, Enums.TypeName.Steel, Enums.TypeName.Fairy],
            [Enums.TypeName.Poison]
        )
        self.Fairy    = Type(
            Enums.TypeName.Fairy,
            [Enums.TypeName.Poison, Enums.TypeName.Steel],
            [Enums.TypeName.Fighting, Enums.TypeName.Bug, Enums.TypeName.Dark],
            [Enums.TypeName.Dragon]
        )
        