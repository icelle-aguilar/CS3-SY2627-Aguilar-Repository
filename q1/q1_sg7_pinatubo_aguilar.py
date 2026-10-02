class Glassware:
    def __init__(self, kindofglassware):
        self.kindofglassware = kindofglassware
    def __del__(self):
        print(f"A {self.kindofglassware} was lost.")

class Beaker(Glassware):
    def __init__(self, kindofglassware="Beaker"):
        super().__init__(kindofglassware)


class Tray:
    def __init__(self):
        self.beakers = [Beaker() for _ in range(5)]
        
    def __del__(self):
        print("A Tray was deleted.")
tray1 = Tray()

print(f"There are {len(tray1.beakers)} beakers.")
del tray1