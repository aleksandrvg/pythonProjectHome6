from classLibrary.BaseModel import BaseModel
from classLibrary.User import User
from classLibrary.Car import Car
from peewee import *


class UserToCar(BaseModel):
    id = PrimaryKeyField(column_name="id")
    user = ForeignKeyField(User, related_name="user_id_user_to_car", to_field="id")
    car = ForeignKeyField(Car, related_name="car_id_user_to_car", to_field="id")
    date = DateField(column_name="date_of_give")
    hour = TimeField(column_name="hour_of_give")
    term = TimeField(column_name="term_of_give")

    class Meta:
        table_name = "user_to_car"
