from classLibrary.User import User


def RegistrationUser(phone, first_name, second_name, third_name=None):
    user = User(phone_number=phone, first_name=first_name, second_name=second_name, third_name=third_name)
    user.save()
    return user


def FindByPhone(phone):
    user = User.select().where(User.phone_number == phone).get()
    return user

