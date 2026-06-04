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

    # --- Getters (Accessors) ---
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

if __name__ == "__main__":
    print("🐾 Welcome to the Pet Registration Portal 🐾\n")

    # Initialize object
    my_pet = Pet()

    # User Input
    name_input = input("Enter your pet's name: ").strip()
    type_input = input("Enter your pet's type (e.g., Dog, Cat, Bird): ").strip()
    age_input = input("Enter your pet's age: ").strip()

    # Mutator assignment
    my_pet.set_name(name_input)
    my_pet.set_animal_type(type_input)
    my_pet.set_age(age_input)

    # Accessor display
    print("\n --- REGISTERED PET PROFILE ---")
    print(f" Name       : {my_pet.get_name()}")
    print(f" Type       : {my_pet.get_animal_type()}")
    print(f" Age        : {my_pet.get_age()} year(s) old")
    print("═" * 33)