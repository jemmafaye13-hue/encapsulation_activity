class Car:
    def __init__(self, year_model, make):
        """Constructor initializing private attributes and setting speed to 0."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        """Accelerate the car by adding 5 to the current speed."""
        self.__speed += 5

    def brake(self):
        """Brake the car by subtracting 5, ensuring speed doesn't drop below 0."""
        self.__speed = max(0, self.__speed - 5)

    