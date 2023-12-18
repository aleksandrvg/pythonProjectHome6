from classLibrary.BaseModel import BaseModel
from peewee import *


class Car(BaseModel):
    id = PrimaryKeyField(column_name="id")
    model = CharField(column_name="model", max_length=50)

    class Meta:
        table_name = "car"
