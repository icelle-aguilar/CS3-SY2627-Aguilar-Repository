class Car:
    def __init__(self,brand,model,battery=35):
        self.brand=brand
        self.model=model
        self.battery=battery
        print(f"You've created a {self.brand}, {self.model}")
    def go(self,distance):
        self.battery-=distance/20
        print(f"The car traveled {distance} km")
        print(f"You have {self.battery} wH left")
    def charge(self,wH):
        self.battery+=wH
        print(f"Car recharged. You now have {self.battery} wH")
    def dashboard(self):
        print(f"Battery: {self.battery}")
    def getBattery():
        return self.battery
    
car1=Car("Toyota","Rush")
car1.go(67)
car1.charge(40)
car1.dashboard

while car1.battery > 0:
    act=input("What do you want to do? (g or c): ")
    if act.startswith("g"):
        distance=int(input("How far? "))
        car1.go(distance)
    elif act.startswith("c"):
        wH=int(input("How much to charge? "))
        car1.charge(wH)
else:
    print("Invalid action")

print("Game over. You ran out of batteries")
