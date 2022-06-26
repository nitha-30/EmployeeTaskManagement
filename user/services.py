from user.models import User

def create_user(data):
    password = data.pop("password", None)
    user = User.objects.create(**data)
    user.set_password(password)
    user.is_active = True
    user.save()
    return user
