class Thermometer:

    def __init__(self):

        print("A thermometer is ready to measure temperature.")


    def measure(self, temperature):

        print(f"The thermometer reads {temperature}°C.")


class Scientist:

    def __init__(self, name):

        self.name = name

        print(f"Scientist {self.name} is ready for experiments.")


    def conduct_experiment(self, thermometer):

        print(f"{self.name} is conducting an experiment.")

        # Dependency: Scientist uses the Thermometer temporarily

        thermometer.measure(37)


# Example usage

thermo = Thermometer()

scientist = Scientist("Dr. Reyes")


scientist.conduct_experiment(thermo)


# Notice: The Scientist does not own the Thermometer.

# Even if the Scientist object is deleted, the Thermometer still exists.

del scientist


thermo.measure(25)  # Thermometer can still be used independently

