from enum import Enum,unique

@unique
class Vip(Enum):
    YELLOW = 1
    GREEN  = 1
    BLACK  = 3
    RED    = 4

for v in Vip.__members__:
    print(v)

print(Vip(1))
