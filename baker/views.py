from django.shortcuts import render
from home.models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake
from django.contrib.auth.models import User
from django.contrib import auth

#make_password(str) : 이 함수에 넣어준 문자열을 암호화합니다. (hashing)
#check_password(a,b) : a,b가 일치하는지 확인, 반환합니다.
from django.contrib.auth.hashers import make_password, check_password

################################
# 이메일 인증 백엔드 구역이래요!!!! #
################################

from django.http import HttpResponse, JsonResponse
# Create your views here.

def signUp(request):
    if request.method == 'POST':
        username = request.POST.get['']
        # 비밀번호 이미 확인된 상태라 필요없음.
        if request.POST["password_baker"] == request.POST["re-password_baker"]:
            bakerUser = Baker.objects.create()

            bakerUser.save()
    return render(request, 'baker/signUp_baker.html')



def login(request):
    #person = Baker
    #person.email = request.GET('email')
    #person.password = request.GET('password')
    return render(request, 'baker/login_baker.html')

def idpw_search(request):
    return render(request, 'baker/idpw_search_baker.html')

def valid(request): #사업자번호확인 -> join
    return HttpResponse("Valid page!")






# 가게 관리
def enrollStore(request):
    return render(request, 'baker/enrollStore.html')
def opendays(request):
    return render(request, 'baker/opendays.html')
def storeReview(request):
    return render(request, 'baker/storeReview.html')

# 케이크 관리
def myCakes(request):
    return render(request, 'baker/myCakes.html')
def options(request):
    return render(request, 'baker/options.html')


def manageOrder(request):
    return render(request, 'baker/manageOrder.html')

def mypage(request):
    return render(request, 'baker/mypage_baker.html')
