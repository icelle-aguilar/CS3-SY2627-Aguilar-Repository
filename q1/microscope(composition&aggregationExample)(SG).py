# --- INHERITANCE SECTION ---


class Microscope:

    def __init__(self, magnification, lens_type):

        # General attributes shared by all microscopes

        self.magnification = magnification

        self.lens_type = lens_type


    def view(self):

        print(f"Viewing through {self.lens_type} lenses at {self.magnification} magnification.")


class DigitalMicroscope(Microscope):

    def __init__(self, magnification, lens_type, sensor_resolution):

        # Pass general data up to the Parent (Microscope)

        super().__init__(magnification, lens_type)

        # Add specific child attributes

        self.sensor_resolution = sensor_resolution


    def capture_image(self):

        print(f"Capturing image with {self.sensor_resolution} resolution.")


    def record_video(self):

        print("Recording digital video...")
