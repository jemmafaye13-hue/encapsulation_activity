class Car:
    def __init__(self, year_model, make):
        """Constructor initializing private attributes and setting speed to 0."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

        