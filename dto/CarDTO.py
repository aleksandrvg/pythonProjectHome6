from classLibrary.Car import Car


def GetAllCar() -> list:
    cars = Car.select().dicts()
    returnCar = []
    for car in cars:
        returnCar.append(Car(id=car["id"], model=car["model"]))
    return returnCar


def GetCarById(Id:int) -> Car:
    car = Car.select().where(Car.id == Id).get()
    return car

