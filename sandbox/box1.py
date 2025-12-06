from enum import Enum

class EffectType(Enum):
    NULL = 0

    CREATE_THING = 1

    CHG_PROP_ADD = 10
    CHG_PROP_SUB = 11
    CHG_PROP_MUL = 12
    CHG_PROP_DIV = 13

class Effect:
    etype: EffectType
    params: list[object]

    def __init__(self, etype: EffectType, *params):
        self.etype = etype
        self.params = params

    def __str__(self):
        return f'{str(self.etype)}, {str(self.params)}'

    def __repr__(self):
        return f'{str(self.etype)}, {str(self.params)}'

class Trigger:
    effects: list[Effect]

    def __init__(self, effects):
        self.effects = effects
    
    def __str__(self):
        return str(self.effects)

    def __repr__(self):
        return str(self.effects)

class Thing:
    props: dict[str, object]
    triggers: dict[str, Trigger]

    def __init__(self, props, triggers):
        self.props = props
        self.triggers = triggers

    def activate_effect(self, name):
        return self.triggers[name]

e1 = Effect(EffectType.CHG_PROP_SUB, 'hp', 1)
t1 = Trigger([e1])
trigs = {'primary': t1}
default_weapon = Thing({}, trigs)

print(default_weapon.activate_effect('primary'))

class EffectProcessor:
    def __init__(self):
        pass

class Actor:
    things: dict[str, Thing]
    props: dict[str, object]

    def __init__(self):
        self.things = {}
    
    def add_thing(self, name, thing):
        self.things[name] = thing

    def process_effect(self, effect):
        pass

player = Actor()
player.add_thing('weapon', default_weapon)