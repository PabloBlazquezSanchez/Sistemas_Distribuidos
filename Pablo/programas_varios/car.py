from vehiculo import Vehicle

class Car(Vehicle):
    person_price = 20

    def __init__(self, capacity):
        super().__init__(capacity)