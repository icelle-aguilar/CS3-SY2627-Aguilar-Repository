class Glassware:
    def __init__(self, kindofglassware):
        self.kindofglassware = kindofglassware


class Beaker(Glassware):
    def __init__(self, kindofglassware):
        super().__init__(kindofglassware)


class Tray:
    def __init__(self):
        self.beakers = [Beaker() for _ in range(5)]