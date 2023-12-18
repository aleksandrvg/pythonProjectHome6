from classLibrary.UserToCar import UserToCar
from classLibrary.User import User
from classLibrary.Car import Car
import datetime


def IssuedCar(user: User, car: Car) -> UserToCar:
    dateOfGive = datetime.datetime.now().strftime("%Y-%m-%d")
    hourOfGive = datetime.datetime.now().strftime("%H:%M:%S")
    termOfGive = datetime.datetime.now().strftime("%H:%M:%S")
    newIssued = UserToCar(date=dateOfGive, hour=hourOfGive, term=termOfGive, user=user, car=car)
    newIssued.save()
    return newIssued


def GetIssuedCarByUserPhone(phone: str) -> list:
    rezIssuedCar = []
    IssuedCars = UserToCar().select().where(UserToCar.user.phone == phone).dicts
    for issuedCar in IssuedCars:
        rezIssuedCar.append(UserToCar(id=issuedCar["id"], date=issuedCar["date"], car=issuedCar["car"]))
    return rezIssuedCar
