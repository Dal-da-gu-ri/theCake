from home.models import *

def secureID(userid,reviewNum):
    customer = Orderer.objects.get(pk=userid)
    review = Review.objects.get(pk=reviewNum)
    if len(userid)>3:
        firstthree = customer.user_ID[0]+customer.user_ID[1]+customer.user_ID[2]
        review.secureID = firstthree+"***"
        review.save()
    else:
        firstletter = customer.user_ID[0]
        review.secureID = firstletter+"***"
        review.save()