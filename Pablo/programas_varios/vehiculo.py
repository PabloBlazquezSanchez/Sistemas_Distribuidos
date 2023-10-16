class Vehicle:
    person_price = 10 #* €/person
    def __init__(self, capacity):
        self.capacity = capacity
    
    def fare_price(self):
        return self.capacity * self.person_price

vehicle = Vehicle(6)

print("Vehicle capacity is: ", vehicle.capacity)
# vehicle.person_price = 200
print("Vehicle fare price is: ", vehicle.fare_price())