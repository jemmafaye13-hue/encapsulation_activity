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
        