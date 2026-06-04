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

    # --- Accessors ---
    def get_speed(self):
            return self.__speed

    def get_car_info(self):
        return f"{self.__year_model} {self.__make}"

if __name__ == "__main__":
    import time

    # Create Car Object
    my_car = Car ("2026", "Nissan GT-R")
    print(f"🚗 Testing performance specs for: {my_car.get_car_info()}\n")

    # Accelerating 5 times
    print("⚡ Pushing the gas pedal (Accelerating)...")
    for i in range(1, 6):
        my_car.accelerate()
        time.sleep(0.2)
        print(f"   Hit {i}: Current Speed = {my_car.get_speed()} km/h")

    print("\n🛑 Slamming on the brakes...")
    # Braking 5 times
    for i in range(1, 6):
        my_car.brake()
        time.sleep(0.2)
        print(f"   Brake {i}: Current Speed = {my_car.get_speed()} km/h")