import random
import string

def newcakepk():
    newpk = ''.join(random.choice(string.ascii_letters+string.digits)for _ in range(10))
    return newpk