print(f"{"-"*36}\n")


# ACTIVITY 3

class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")
class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")
class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()
    
w=Warrior()
m=Mage()
a=Archer()

characters=[w,m,a]

for c in characters:
    perform_move(c)


print(f"\n{"-"*36}\n")


# ACTIVITY 4

class HealthPotion:
    def use(self):
        print("You regain 50 HP!")
class ManaPotion:
    def use(self):
        print("You restore 30 MP")
class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")

def apply_item(item):
    item.use()
    
hp=HealthPotion()
mp=ManaPotion()
sb=SpeedBoost()

potions=[hp,mp,sb]

for p in potions:
    apply_item(p)


print(f"\n{"-"*36}\n")


# ACTIVITY 5
print("1. hi")
print("2. hi")
print("3. hi")


print(f"\n{"-"*36}")
