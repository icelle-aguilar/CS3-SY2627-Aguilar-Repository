from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH"

tempSensor=TempSensor()
phSensor=PHSensor()

print(f"--- Lab Inventory System ---")
print(f"[pH Sensor] Reading: {phSensor.get_reading()} (Neutral)")
print(f"[Temperature Sensor] Reading: {tempSensor.get_reading()}")
print(f"\n----------------------------")
