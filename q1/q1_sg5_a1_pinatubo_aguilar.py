class Hero:
  def __init__(self, name, hp):
    self.name=name
    self.hp=100
  def take_damage(self, amount):
    self.hp-=amount

arthur=Hero("Arthur", 100)
morgana=Hero("Morgana", 100)

hit=arthur.take_damage(10)

print(f"Arthur's HP: {arthur.hp}\nMorgana's HP: {morgana.hp}")
