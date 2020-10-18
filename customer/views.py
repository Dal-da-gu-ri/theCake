from django.shortcuts import render, redirect
from home.models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake, checkOrderer
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def main(request):
    return render(request, 'customer/main_customer.html')

def join(request):
    #global bsID, emailBaker
    if request.method == "GET":
        return render(request, 'customer/join_customer.html')
    elif request.method == "POST":
        userID = request.POST.get('ID_customer',None)
        namecustomer = request.POST.get('name_customer',None)
        passwordcustomer = request.POST.get('password_customer',None)
        phoneNumcustomer = request.POST.get('phoneNum_customer',None)
        res_data = {}
        try:
            curCustomer = checkOrderer.objects.get(userID = userID)
            customerEmail = curCustomer.useremail
            customer = Orderer(
                userID = userID,
                email = customerEmail,
                name = namecustomer,
                phoneNum = phoneNumcustomer,
                password = make_password(passwordcustomer)
            )
            customer.save()
            return redirect('/customer/login')
            #return render(request, 'fuser/login.html')
        except checkOrderer.DoesNotExist:
            # comment = None
            res_data['error'] = "등록되지 않은 아이디입니다."
            return render(request, 'customer/join_customer.html', res_data)

def useridCheck(request):
    #global bsID
    if request.method == "GET":  # url을 이용한 방법
        return render(request, 'customer/useridCheck.html')
    elif request.method == "POST":  # 등록 버튼을 사용한 방법기
        userID = request.POST.get('ID_customer',None)
        userEmail = request.POST.get('email_customer', None)
        res_data = {}

        try:
            customer = checkOrderer.objects.get(userid = userID)
            res_data['error'] = "이미 등록된 아이디입니다."
            return render(request, 'customer/useridCheck.html', res_data)
        except checkOrderer.DoesNotExist:
            #comment = None
            checkorderer = checkOrderer(
                userid=userID,
                useremail=userEmail
            )
            checkorderer.save()
            return redirect('/customer/signUp/join')
                #return render(request, 'baker/join_baker.html')

def login(request):
    if request.method=="GET":
        return render(request,'customer/login_customer.html')
    elif request.method == "POST":
        #전송받은 이메일 비밀번호 확인
        userID = request.POST.get('ID_customer')
        password = request.POST.get('password')

        #유효성 처리
        res_data={}
        if Orderer.objects.filter(userID=userID).exists():
            #res_data['error']="모든 칸을 다 입력해주세요"
            orderer = Orderer.objects.get(userID=userID)
            if check_password(password,orderer.password):
                #응답 데이터 세션에 값 추가. 수신측 쿠키에 저장됨
                #request.session['user']=baker.id
                request.session['user']=orderer.userID

                #리다이렉트
                return redirect('/') #urls에 정의해둔 home으로
                #return render(request,'fuser/loginsuccess.html',res_data)
            else:
                res_data['error'] = "비밀번호가 틀렸습니다."
                return render(request, 'customer/login_customer.html', res_data)

        else:
            res_data['error'] = "존재하지 않는 아이디입니다."
            return render(request,'customer/login_customer.html',res_data)


# login에 성공하면 main_customer.html으로 이동!
def main(request):
    return render(request, 'customer/main_customer.html')

def testing(request):

    return render(request,'customer/test.html')

def orderlist(request):
    return render(request, 'customer/orderlist_customer.html')


def mypage(request):
    return render(request, 'customer/mypage_customer.html')