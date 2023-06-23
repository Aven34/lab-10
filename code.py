## Фабрика

```
class Car:
    def drive(self):
        print("Driving a car...")

class Bike:
    def ride(self):
        print("Riding a bike...")

class VehicleFactory:
    def createVehicle(self, vehicleType):
        if vehicleType == "car":
            return Car()
        elif vehicleType == "bike":
            return Bike()

factory = VehicleFactory()

car = factory.createVehicle("car")
car.drive()

bike = factory.createVehicle("bike")
bike.ride()
```

## Абстрактная фабрика

```
class Car:
    def drive(self):
        print("Driving a car...")

class Bike:
    def ride(self):
        print("Riding a bike...")

class VehicleFactory:
    def createCar(self):
        pass
    
    def createBike(self):
        pass

class CarFactory(VehicleFactory):
    def createCar(self):
        return Car()

class BikeFactory(VehicleFactory):
    def createBike(self):
        return Bike()

carFactory = CarFactory()
car = carFactory.createCar()
car.drive()

bikeFactory = BikeFactory()
bike = bikeFactory.createBike()
bike.ride()
```

## Строитель

```
class Car:
    def __init__(self):
        self.color = None
        self.engine = None
        self.wheels = None

    def __str__(self):
        return f"Car with color {self.color}, engine {self.engine} and {self.wheels} wheels"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def setColor(self, color):
        self.car.color = color
        return self
    
    def setEngine(self, engine):
        self.car.engine = engine
        return self

    def setWheels(self, wheels):
        self.car.wheels = wheels
        return self

    def getResult(self):
        return self.car

builder = CarBuilder()
car = builder.setColor("red").setEngine("V8").setWheels(4).getResult()
print(car)
