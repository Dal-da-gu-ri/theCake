import string, random

def passwordMaker():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(random.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
            break


    return password