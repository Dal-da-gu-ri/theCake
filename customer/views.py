from django.shortcuts import render, redirect
from home.models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def main(request):
    return render(request, 'customer/main_customer.html')

"""
def emailValid(request):
    #이메일 저장된거랑 확인해서 중복된거 있는지
    if request.method == 'GET':
        if Orderer.objects.filter(email__exact=request.GET["email"]) == False:
            customerUser = Orderer.objects.create
            customerUser.email = request.GET["email"]
            customerUser.save()

            # return render(request, '') 이메일 사용가능
        else:
            # return 다른 이메일을 입력해주세요
            return render(request, 'customer/login_customer.html')

def passwordCheck(request):
    #비밀번호 입력 확인
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["confirm"]:
            customerUser = Orderer.objects.get(pk=request.GET["email"])
            customerUser.password = request.POST["password1"]
            customerUser.save()

            # 비밀번호 확인
        else:
            # 입력한 비밀번호를 다시 확인해주세요
            return render(request, 'customer/login_customer.html')

def signup(request):
    if request.method == 'POST':
        if Orderer.objects.filter(email__exact=request.POST["email"]) == False:
            if request.POST["password1"] == request.POST["confirm"]:
                customerUser = Orderer.objects.create
                customerUser.email = request.POST["email"]
                customerUser.name = request.POST["name"]
                customerUser.phoneNum = request.POST["Phone"]
                customerUser.password = request.POST["password1"]
                customerUser.save()

                return render(request, 'customer/test.html')


"""


def signUp(request):
    # validemail = None
    res_data = {}
    if request.method == "GET":
        return render(request, 'customer/signUp_customer.html')
    elif request.method == "POST" and 'btn-email' in request.POST:
        email_customer = request.POST.get('email_customer', None)
        if Orderer.objects.filter(email=email_customer).exists():
            # email_fail
            # validemail = False
            res_data['check_email'] = "false"
            # return render(request,'customer/signUp_customer.html', {'check_email':validemail})
        else:
            # email_success
            # validemail = True
            res_data['check_email'] = "true"
            # render(request,'customer/signUp_customer.html',  {'check_email':validemail})
    elif request.method == "POST" and 'submit' in request.POST:
        name_customer = request.POST.get('name_customer', None)
        email_customer = request.POST.get('email_customer', None)
        password_customer = request.POST.get('password_customer', None)
        re_password_customer = request.POST.get('re-password_customer', None)
        phoneNum_customer = request.POST.get('phoneNum_customer', None)

        """
        if not name_customer and email_customer and password_customer and re_password_customer and phoneNum_customer:
            # 모든 값을 입력해야한다는 경고문
        else:
            customer = Orderer(
                email = email_customer,
                name = name_customer,
                phoneNum = phoneNum_customer,
                password = password_customer
            )

            customer.save()

        """
        customer = Orderer(
            email=email_customer,
            name=name_customer,
            phoneNum=phoneNum_customer,
            password=password_customer
        )

        customer.save()

        return render(request, 'customer/signUp_customer.html')
    return render(request, 'customer/signUp_customer.html')
#def signUp(request):
#    return render(request, 'customer/signUp_customer.html')

def login(request):
    return render(request, 'customer/login_customer.html')

# login에 성공하면 main_customer.html으로 이동!
def main(request):
    return render(request, 'customer/main_customer.html')

def testing(request):

    return render(request,'customer/test.html')

def orderlist(request):
    return render(request, 'customer/orderlist_customer.html')


def mypage(request):
    return render(request, 'customer/mypage_customer.html')