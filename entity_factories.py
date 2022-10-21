from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

thief = Actor(
    char="t",
    color=(127, 127, 127),
    name="Thief",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=6, defense=0, power=3),
)
gang_member = Actor(
    char="G",
    color=(150, 150, 150),
    name="Gang Member",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)
