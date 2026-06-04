class Pet:
    def __init__(self):
        """Constructor initializing empty private fields."""
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # --- Setters (Mutators) ---
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        try:
            self.__age = int(age)
        except ValueError:
            print(" Age must be an integer numeric value. Defaulted to 0.")
            self.__age = 0