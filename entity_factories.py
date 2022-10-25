from components.ai import HostileEnemy
from components.consumable import HealingConsumable
from components.fighter import Fighter
from entity import Actor, Item
from components.inventory import Inventory

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
)

thief = Actor(
    char="t",
    color=(127, 127, 127),
    name="Thief",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=6, defense=0, power=3),
    inventory=Inventory(capacity=0),
)
gang_member = Actor(
    char="G",
    color=(150, 150, 150),
    name="Gang Member",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
)

health_potion = Item(
    char="!",
    color=(255, 10, 10),
    name="Medkit",
    consumable=HealingConsumable(amount=4),
)
