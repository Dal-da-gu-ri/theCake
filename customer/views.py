from django.shortcuts import render, redirect, get_object_or_404
from home.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from .color import matchcolor
# Create your views here.
from home.tokens import account_activation_token
from .textCustomer import messageSend
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_text
from django.views.decorators.csrf import csrf_exempt
from baker.forms import *
from customer.forms import *
from .mappingdate import mappingDate

def temp(request):
    return render(request, 'customer/showCakes.html')

def showStores2(request):
    search_key1 = request.GET['search_key1']
    search_key2 = request.GET['search_key2']
    search_key3 = request.GET['search_key3']
    search_key4 = request.GET['search_key4']
    context = { 'search_key1':search_key1, 'search_key2':search_key2, 'search_key3':search_key3, 'search_key4':search_key4 }
    # print(context)
    return render(request,'customer/showStores2.html',context)

@csrf_exempt
def main(request):
    return render(request, 'customer/main_customer.html')

def join(request):
    res_data = {}

    if request.method == "GET":
        customerform = OrdererForm()
        res_data['customer'] = customerform

        return render(request, 'customer/join_customer.html', res_data)
    elif request.method == "POST":
        customerform = OrdererForm(request.POST)
        if customerform.is_valid():  # 유효성 검사

            try:
                curCustomer = checkOrderer.objects.get(userid=customerform.cleaned_data['userID'])
                # crnNum = curBaker.businessCRN

                try:
                    newCustomer = Orderer.objects.get(userID = customerform.cleaned_data['userID'])
                    res_data['error'] = "이미 가입된 계정입니다."
                    return render(request, 'customer/join_customer.html', res_data)

                except Orderer.DoesNotExist:

                    customerobject = Orderer(
                        userID = customerform.cleaned_data['userID'],
                        email = request.POST.get('email_customer',None),
                        name = customerform.cleaned_data['name'],
                        phoneNum = customerform.cleaned_data['phoneNum'],
                        password = make_password(request.POST.get('password_customer',None))
                    )

                    customerobject.save()
                    # res_data['baker']=bakerform
                    current_site = get_current_site(request)
                    message = messageSend(current_site.domain,
                                          urlsafe_base64_encode(force_bytes(customerobject.pk)).encode().decode(),
                                          account_activation_token.make_token(customerobject))
                    mail_subject = "[The Cake] 회원가입 인증 메일입니다."
                    user_email = customerobject.email
                    email = EmailMessage(mail_subject, message, to=[user_email])
                    email.send()
                    res_data['comment'] = user_email + " 로 이메일이 발송되었습니다. \n\n인증을 완료해주세요 :)"
                    return render(request, 'customer/userEmailSent.html', res_data)

            except checkOrderer.DoesNotExist:
                res_data['error'] = "등록되지 않은 아이디입니다."
                return render(request, 'customer/join_customer.html', res_data)
        else:
            # print(storeform.errors)
            return redirect('/baker/inappropriateApproach')

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

def activate(request,uid64, token):
    res_data = {}
    uid = force_text(urlsafe_base64_decode(uid64))
    customer = Orderer.objects.get(pk=uid)

    if customer is not None and account_activation_token.check_token(customer,token):
        customer.is_active = True
        customer.save()
        if request.method == "GET":
            res_data['comment'] = customer.userID+"님의 계정이 활성화되었습니다."
            return render(request,'customer/userActivate.html',res_data)
    elif request.method == "POST":
        return redirect('/customer/login')
    else:
        return redirect('/customer/inappropriateApproach')
        #return HttpResponse('비정상적인 접근입니다.')

def wrongApproach(request):
    if request.method == "GET":
        res_data = {}
        res_data['comment'] = "잘못된 접근입니다."
        return render(request, 'customer/inappropriateApproach.html',res_data)
    elif request.method == "POST":
        return redirect('/')

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
            orderer = Orderer.objects.get(userID=userID)
            if orderer.is_active:
                if check_password(password,orderer.password):
                    request.session['user']=orderer.userID

                    #return render(request,'customer/main_customer.html')  ####여기가 안됨
                    return redirect('/customer/main')
                else:
                    #res_data['error'] = "비밀번호가 틀렸습니다."
                    res_data['error'] = "아이디/비밀번호 오류"
                    return render(request, 'customer/login_customer.html', res_data)
            else:
                res_data['error'] = "계정을 활성화해주세요."
                return render(request, 'customer/login_customer.html', res_data)
        else:
            #res_data['error'] = "존재하지 않는 아이디입니다."
            res_data['error'] = "아이디/비밀번호 오류"
            return render(request,'customer/login_customer.html',res_data)


# # login에 성공하면 main_customer.html으로 이동!
def main_customer(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        customer = Orderer.objects.get(pk=user_id)
        res_data['customername'] = customer.name
        if request.method == 'GET':
            #print("get")

            return render(request, 'customer/main_customer.html',res_data)
        elif request.method == 'POST':
            request.session['sido'] = request.POST.get('sido', None)
            request.session['sigungu'] = request.POST.get('sigungu', None)
            request.session['dong'] = request.POST.get('dong', None)
            # request.session['date'] = request.POST.get('date', None)

            #날짜도 받도록 해야함
            #print(request.session.get('sido'))
            #print("post")
            #return redirect('/customer/stores', res_data)
            #print("sido: "+request.session.get('sido'))
            #print("sigungu: " + request.session.get('sigungu'))
            # if request.session.get('sigungu'):
            #     print("exist")
            # else:
            #     print("not exist")
            #return HttpResponse(request.session.get('sido')+" "+request.session.get('sigungu')+" "+request.session.get('dong'))
            #return HttpResponse(user_id)

            # print(request.session.get['date'])
            return redirect('/customer/main/stores', res_data)

    else:
        if request.method == "GET":
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'customer/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/customer/login')

    #return render(request, 'customer/main_customer.html')


def showStores(request):
    res_data = {}
    user_id = request.session.get('user')
    if user_id:

        customer = Orderer.objects.get(pk=user_id)
        res_data['customername'] = customer.name
        # sido = request.session.get('sido')
        # gungu = request.session.get('gungu')
        # dong = request.session.get('dong')

        sido = request.GET['sido']
        sigugun = request.GET['sigugun']
        dong = request.GET['dong']
        day = request.GET['date']
        res_data = {'sido': sido, 'sigugun': sigugun, 'dong': dong, 'date': day}
        orderdate = request.GET['date']
        # ordermonth = int(orderdate[5])*10+int(orderdate[6])
        # orderday = int(orderdate[8])*10+int(orderdate[9])
        # print(orderdate[4])
        store_list=[]
        isStore = False

        if day:
            orderyear = int(orderdate[0])*1000+int(orderdate[1])*100+int(orderdate[2])*10+int(orderdate[3])
            ordermonth = int(orderdate[5]) * 10 + int(orderdate[6])
            orderday = int(orderdate[8]) * 10 + int(orderdate[9])
            request.session['selectedYear'] = orderyear
            request.session['selectedMonth'] = ordermonth
            request.session['selectedDay'] = orderday

            if sido:
                if sigugun:
                    if dong:
                        # store_list = Store.objects.filter(daum_sido=sido, daum_sigungu=sigugun, daum_dong=dong)

                        stores = Store.objects.filter(daum_sido=sido, daum_sigungu=sigugun, daum_dong=dong)
                        for store in stores:
                            if mappingDate(store,ordermonth,orderday) ==True: # 주문가능한 수량이 있을경우
                                storeobject = Store.objects.get(businessID = store)
                                store_list.append(storeobject)
                                isStore = True

                        if isStore == True:
                            res_data['happy'] = "조회된 가게 있음."
                        else:
                            res_data['error'] = "조회된 가게가 없습니다."

                        # print(store_list)

                    else:
                        stores = Store.objects.filter(daum_sido=sido, daum_sigungu=sigugun)
                        for store in stores:
                            if mappingDate(store,ordermonth,orderday) ==True: # 주문가능한 수량이 있을경우
                                storeobject = Store.objects.get(businessID = store)
                                store_list.append(storeobject)
                                isStore = True

                        if isStore == True:
                            res_data['happy'] = "조회된 가게 있음."
                        else:
                            res_data['error'] = "조회된 가게가 없습니다."

                else:
                    stores = Store.objects.filter(daum_sido=sido)
                    for store in stores:
                        if mappingDate(store, ordermonth, orderday) == True:  # 주문가능한 수량이 있을경우
                            storeobject = Store.objects.get(businessID=store)
                            store_list.append(storeobject)
                            isStore = True

                    if isStore==True:
                        res_data['happy']="조회된 가게 있음."
                    else:
                        res_data['error'] = "조회된 가게가 없습니다."


        else:             #선택된 가게가 없는 데 넘어온 경우..
            res_data['error'] = "날짜를 선택해주세요."
             # return HttpResponse(user_id)

        res_data['store_list'] = store_list


        # print(isStore)
        # return render(request, 'customer/showStores.html', res_data)
        return render(request, 'customer/stores.html', res_data)
        # return render(request,'customer/showStores2.html',res_data)


    else:
        if request.method == "GET":
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'customer/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/customer/login')

    #return render(request,'customer/showStores.html')


def storeInfo(request,pk):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        customer = Orderer.objects.get(pk=user_id)
        res_data['customername'] = customer.name
        storeobject = get_object_or_404(Store,pk=pk)

        if request.method == "GET":
            storeform = StoreForm(instance=storeobject)
            # cakeform = CakeForm()
            res_data['store'] = storeform

            store_list = Store.objects.filter(pk=pk)
            res_data['store_list'] = store_list
            cake_list = Cake.objects.filter(crn=storeobject.businessID)
            res_data['cake_list'] = cake_list
            res_data['selectedYear']=request.session.get('selectedYear')
            res_data['selectedMonth']=request.session.get('selectedMonth')
            res_data['selectedDay']=request.session.get('selectedDay')

            # print(res_data)
            # return render(request, 'customer/showStores.html', res_data)
            return render(request,'customer/showCakes.html',res_data)
        elif request.method == "POST":
            ## 케이크 가게가 마음에 들어서 주문하러 기
            return render(request,'customer/showCakes.html',res_data)


            return render(request, 'customer/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/customer/login')


    else:
        if request.method == "GET":
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'customer/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/customer/login')

def cakeOrder(request,crn,cakepk):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        customer = Orderer.objects.get(pk=user_id)
        res_data['customername'] = customer.name

    print("Hello")
    print(crn)
    print(cakepk)

    return render(request, 'customer/orderCake.html', res_data)
    #   주문화면

def testing(request):

    return render(request,'customer/test.html')

def orderlist(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        customer = Orderer.objects.get(pk=user_id)
        res_data['customername'] = customer.name

    return render(request, 'customer/orderlist_customer.html',res_data)


def mypage(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        customer = Orderer.objects.get(pk=user_id)
        res_data['customername'] = customer.name

    return render(request, 'customer/mypage_customer.html',res_data)


def logout(request):
    res_data = {}

    if request.method == "GET":
        if request.session['user']:
            user_id = request.session.get('user')
            customer = Orderer.objects.get(pk=user_id)
            del (request.session['user'])
            res_data['comment'] = customer.name + " 님의 계정이 성공적으로 로그아웃되었습니다!"
            return render(request, 'customer/logout_customer.html', res_data)
        else:
            return redirect('/customer/inappropriateApproach')
    elif request.method == "POST":
        return redirect('/')



def wrongApproach(request):
    if request.method == "GET":
        res_data = {}
        res_data['comment'] = "잘못된 접근입니다."
        return render(request, 'customer/inappropriateApproach.html',res_data)
    elif request.method == "POST":
        return redirect('/')