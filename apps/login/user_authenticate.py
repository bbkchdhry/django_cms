from django.forms import model_to_dict
from apps.account.hashing import hash_string

from apps.account.models import User

def authenticate(email, password):
    try:
        user = User.objects.get(email=email)
        salt = user.salt
        hash = user.hashed_password
        if hash_string(salt, password) == hash:
            return user
        else:
            return False
    except User.DoesNotExist as e:
        return False