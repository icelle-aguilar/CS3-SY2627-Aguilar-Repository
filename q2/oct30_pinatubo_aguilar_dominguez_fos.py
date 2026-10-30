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
