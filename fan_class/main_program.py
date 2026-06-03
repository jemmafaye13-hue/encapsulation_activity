class Fan:
    # Class constants for speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        """Constructor with default values."""
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = str(color)
        self.__on = bool(on)

    # --- Getters (Accessors) ---
    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def is_on(self):
        return self.__on

    # --- Setters (Mutators) ---
    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed
        else:
            print("Invalid speed setting!")

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = str(color)

    def set_on(self, on):
        self.__on = bool(on)

    def display_properties(self, name):
        border = "═" * 35
        print(f"\n║ {name.upper() :^31} ║")
        print(border)
        print(f" Status  : {'▶ ON' if self.__on else '🛑 OFF'}")
        print(f" Speed   : {self.__speed}")
        print(f" Radius  : {self.__radius} cm")
        print(f" Color   : {self.__color.capitalize()}")
        print(border)

if __name__ == "__main__":
    print("INITIALIZING FAN TESTS")

    fan1 = Fan(speed=Fan.FAST, radius=10, color="yellow", on=True)
    fan1.display_properties("Fan 1")

    fan2 = Fan(speed=Fan.MEDIUM, radius=5, color="blue", on=False)
    fan2.display_properties("Fan 2")

