from datetime import datetime

def makeordernum():
    num = datetime.today().strftime("%Y%m%d%H%M%S")

    #print(num)
    return num