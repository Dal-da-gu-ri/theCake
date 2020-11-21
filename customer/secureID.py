from home.models import *

def secureID(userid,reviewNum):
    customer = Orderer.objects.get(pk=userid)
    review = Review.objects.get(pk=reviewNum)
    if len(userid)>3:
        firstthree = customer.userID[0]+customer.userID[1]+customer.userID[2]
        review.secureID = firstthree+"***"
        review.save()
    else:
        firstletter = customer.userID[0]
        review.secureID = firstletter+"***"
        review.save()