import random
import string


def generate_random_string(length=8):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_user_data():
    return {
        "email": f"{generate_random_string(8)}@yandex.ru",
        "password": generate_random_string(10),
        "name": f"User_{generate_random_string(5)}",
    }