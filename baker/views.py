from django.shortcuts import render, redirect, get_object_or_404
from home.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from .crn import Search_CRN
import json
from home.tokens import account_activation_token
from .textBaker import messageSend,passwordMessage
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_text
from .forms import *
from datetime import datetime

from .create_password import passwordMaker

from .dailyamounts import setDailyAmounts
#make_password(str) : 이 함수에 넣어준 문자열을 암호화합니다. (hashing)
#check_password(a,b) : a,b가 일치하는지 확인, 반환합니다.

from django.http import HttpResponse, JsonResponse
# Create your views here.

### 회원가입 및 로그인

def join3(request):
    #global bsID, emailBaker
    if request.method == "GET":
        return render(request, 'baker/join_baker.html')
    elif request.method == "POST":
        userid = request.POST.get('userid',None)
        namebaker = request.POST.get('name_baker',None)
        emailbaker = request.POST.get('email_baker',None)
        passwordbaker = request.POST.get('password_baker',None)
        phoneNumbaker = request.POST.get('phoneNum_baker',None)
        res_data = {}
        baker = Baker(
            #businessID=crnNum,
            userID=userid,
            email=emailbaker,
            name=namebaker,
            phoneNum=phoneNumbaker,
            password=make_password(passwordbaker)
        )
        baker.save()

        # store = Store(
        #     businessID=crnNum
        # )
        # store.save()
        current_site = get_current_site(request)
        message = messageSend(current_site.domain,
                              urlsafe_base64_encode(force_bytes(baker.pk)).encode().decode(),
                              account_activation_token.make_token(baker))
        mail_subject = "[The Cake] 회원가입 인증 메일입니다."
        user_email = baker.email
        email = EmailMessage(mail_subject, message, to=[user_email])
        email.send()
        res_data['comment'] = user_email + " 로 이메일이 발송되었습니다. \n\n인증을 완료해주세요 :)"
        return render(request, 'baker/userEmailSent.html', res_data)

def join2(request):
    #global bsID, emailBaker
    if request.method == "GET":
        return render(request, 'baker/join_baker.html')
    elif request.method == "POST":
        userid = request.POST.get('userid',None)
        namebaker = request.POST.get('name_baker',None)
        emailbaker = request.POST.get('email_baker',None)
        passwordbaker = request.POST.get('password_baker',None)
        phoneNumbaker = request.POST.get('phoneNum_baker',None)
        res_data = {}
        try:
            curBaker = checkBaker.objects.get(userid = userid)
            crnNum = curBaker.businessCRN

            try:
                newBaker = Baker.objects.get(userID=userid)
                res_data['error'] = "이미 가입된 계정입니다."
                return render(request, 'baker/join_baker.html', res_data)
            except Baker.DoesNotExist:

                baker = Baker(
                    businessID=crnNum,
                    userID=userid,
                    email=emailbaker,
                    name=namebaker,
                    phoneNum=phoneNumbaker,
                    password=make_password(passwordbaker)
                )
                baker.save()

                store = Store(
                    businessID = crnNum
                )
                store.save()
                current_site = get_current_site(request)
                message = messageSend(current_site.domain,
                                  urlsafe_base64_encode(force_bytes(baker.pk)).encode().decode(),
                                  account_activation_token.make_token(baker))
                mail_subject = "[The Cake] 회원가입 인증 메일입니다."
                user_email = baker.email
                email = EmailMessage(mail_subject, message, to=[user_email])
                email.send()
                res_data['comment'] = user_email+" 로 이메일이 발송되었습니다. \n\n인증을 완료해주세요 :)"
                return render(request,'baker/userEmailSent.html',res_data)
                #return redirect('/baker/login')
                #return render(request, 'fuser/login.html')
        except checkBaker.DoesNotExist:
            # comment = None
            res_data['error'] = "등록되지 않은 아이디입니다."
            return render(request, 'baker/join_baker.html', res_data)

def join(request):
    res_data={}
    if request.method == 'POST':
        bakerform = BakerForm(request.POST)  # ,instance=request.user  ,request.FILES, data
        if bakerform.is_valid():  # 유효성 검사

            try:
                curBaker = checkBaker.objects.get(userid=bakerform.cleaned_data['userID'])
                crnNum = curBaker.businessCRN

                try:
                    newBaker = Baker.objects.get(userID = bakerform.cleaned_data['userID'])
                    res_data['error'] = "이미 가입된 계정입니다."
                    return render(request, 'baker/join_baker.html', res_data)

                except Baker.DoesNotExist:

                    bakerobject = Baker(
                        businessID = curBaker.businessCRN,
                        userID = bakerform.cleaned_data['userID'],
                        email = request.POST.get('email_baker',None),
                        name = bakerform.cleaned_data['name'],
                        phoneNum = bakerform.cleaned_data['phoneNum'],
                        password = make_password(request.POST.get('password_baker',None))
                    )

                    bakerobject.save()
                    # res_data['baker']=bakerform
                    current_site = get_current_site(request)
                    message = messageSend(current_site.domain,
                                          urlsafe_base64_encode(force_bytes(bakerobject.pk)).encode().decode(),
                                          account_activation_token.make_token(bakerobject))
                    mail_subject = "[The Cake] 회원가입 인증 메일입니다."
                    user_email = bakerobject.email
                    email = EmailMessage(mail_subject, message, to=[user_email])
                    email.send()
                    res_data['comment'] = user_email + " 로 이메일이 발송되었습니다. \n\n인증을 완료해주세요 :)"
                    return render(request, 'baker/userEmailSent.html', res_data)

            except checkBaker.DoesNotExits:
                res_data['error'] = "등록되지 않은 아이디입니다."
                return render(request, 'baker/join_baker.html', res_data)
        else:
            # print(storeform.errors)
            return redirect('/baker/inappropriateApproach')

    else:
        # bakerobject = Baker.objects.get(businessID=baker.businessID)
        bakerform = BakerForm()
        # storeform = StoreForm()
        res_data['baker'] = bakerform

        return render(request, 'baker/join_baker.html', res_data)

def login(request):
    if request.method=="GET":
        return render(request,'baker/login_baker.html')
    elif request.method == "POST":
        #전송받은 이메일 비밀번호 확인
        userid = request.POST.get('userid')
        password = request.POST.get('password')

        #유효성 처리
        res_data={}
        if Baker.objects.filter(userID=userid).exists():
            baker = Baker.objects.get(userID=userid)
            if baker.is_active:
                if check_password(password,baker.password):
                    request.session['user']=baker.userID

                #리다이렉트
                    return redirect('/baker/manageStore/enrollStore')
                    #return render(request,'baker/enrollStore.html')
                else:
                    #res_data['error'] = "비밀번호가 틀렸습니다."
                    res_data['error'] = "아이디/비밀번호 오류"
                    return render(request, 'baker/login_baker.html', res_data)
            else:
                res_data['error'] = "계정을 활성화해주세요."
                return render(request, 'baker/login_baker.html', res_data)

        else:
            #res_data['error'] = "존재하지 않는 사업자번호입니다."
            res_data['error'] = "아이디/비밀번호 오류"
            return render(request,'baker/login_baker.html',res_data)

def crnCheck(request):
    if request.method == "GET":  # url을 이용한 방법
        return render(request, 'baker/crnCheck.html')
    elif request.method == "POST":  # 등록 버튼을 사용한 방법기
        bakerid = request.POST.get('userid',None)
        crn = request.POST.get('businessID', None)
        res_data = {}
        try:
            baker = checkBaker.objects.get(userid = bakerid)
            res_data['error'] = "이미 등록된 아이디입니다."
            return render(request, 'baker/crnCheck.html', res_data)

        except checkBaker.DoesNotExist:
            if Search_CRN(crn) == "부가가치세 일반과세자 입니다.":
                try:
                    baker = checkBaker.objects.get(businessCRN=crn)
                    res_data['error'] = "이미 등록된 사업자등록번호입니다."
                    return render(request, 'baker/crnCheck.html', res_data)
                except checkBaker.DoesNotExist:
                    # comment = None
                    checkbaker = checkBaker(
                        userid=bakerid,
                        businessCRN=crn
                    )
                    checkbaker.save()
                    return redirect('/baker/signUp/join')
                    # return render(request, 'baker/join_baker.html')

            else:
                res_data['error'] = "유효하지 않은 사업자등록번호입니다."
                return render(request, 'baker/crnCheck.html', res_data)

def isID(request):
    bakerid = request.POST.get('userid', None)
    res_data = {}
    try:
        baker = Baker.objects.get(userid=bakerid)
        res_data['msg'] = "fail"
        return JsonResponse(res_data)

    except Baker.DoesNotExist:
        res_data['msg'] = "pass"
        return JsonResponse(res_data)

def isEmail(request):
    emailbaker = request.POST.get('email_baker', None)
    res_data = {}
    try:
        baker = Baker.objects.get(email=emailbaker)
        res_data['msg'] = "fail"
        return JsonResponse(res_data)

    except Baker.DoesNotExist:
        res_data['msg'] = "pass"
        return JsonResponse(res_data)

def isCRN(request):
    crn = request.POST.get('businessID', None)
    res_data = {}
    try:
        baker = Baker.objects.get(businessID=crn)
        res_data['msg'] = "fail"
        return JsonResponse(res_data)

    except Baker.DoesNotExist:
        res_data['msg'] = "pass"
        return JsonResponse(res_data)

def activate(request,uid64, token):
    res_data = {}
    uid = force_text(urlsafe_base64_decode(uid64))
    baker = Baker.objects.get(pk=uid)

    if baker is not None and account_activation_token.check_token(baker,token):
        baker.is_active = True
        baker.save()
        if request.method == "GET":
            res_data['comment'] = baker.userID+"님의 계정이 활성화되었습니다."
            return render(request,'baker/userActivate.html',res_data)
    elif request.method == "POST":
        return redirect('/baker/login')
    else:
        return redirect('/baker/inappropriateApproach')

def wrongApproach(request):
    if request.method == "GET":
        res_data = {}
        res_data['comment'] = "잘못된 접근입니다."
        return render(request, 'baker/inappropriateApproach.html',res_data)
    elif request.method == "POST":
        return redirect('/')

def enrollStore(request):
    res_data = {}
    user_id = request.session.get('user')
    #store = StoreForm()
    #return HttpResponse(user_id)

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
        storeobject = Store()
        if request.method == 'POST':
            storeform = StoreForm(request.POST, request.FILES) #,instance=request.user  ,request.FILES, data
            if storeform.is_valid(): #유효성 검사
                    storeobject.businessID = baker.businessID
                    storeobject.manager = baker
                    storeobject.storeName = storeform.cleaned_data['storeName']
                    storeobject.storeContact = storeform.cleaned_data['storeContact']
                    storeobject.pickUpOpen = storeform.cleaned_data['pickUpOpen']
                    storeobject.pickUpClose = storeform.cleaned_data['pickUpClose']
                    storeobject.aboutStore = storeform.cleaned_data['aboutStore']
                    storeobject.postcode = storeform.cleaned_data['postcode']
                    storeobject.address1 = storeform.cleaned_data['address1']
                    storeobject.address2 = storeform.cleaned_data['address2']
                    storeobject.address3 = storeform.cleaned_data['address3']
                    storeobject.location = storeform.cleaned_data['address1'] + " "+storeform.cleaned_data['address2']
                    #storeobject.sido = storeform.cleaned_data['sido']
                    #storeobject.sigugun = storeform.cleaned_data['sigugun']
                    #storeobject.dong = storeform.cleaned_data['dong']
                    storeobject.daum_sido = request.POST.get('daum_sido',None)
                    storeobject.daum_sigungu = request.POST.get('daum_sigungu',None)
                    storeobject.daum_dong = request.POST.get('daum_dong',None)

                    storeobject.storeImg = storeform.cleaned_data['storeImg']

                    storeobject.save()
                    res_data['store'] = storeform
                    res_data['name'] = storeobject.storeImg
                    return render(request, 'baker/enrollStore2.html', res_data)
            else:
                    print(storeform.errors)
                    return redirect('/baker/inappropriateApproach')

        else:
            # storeobject = Store.objects.get(businessID=baker.businessID)
            # storeform = StoreForm(instance=storeobject)
            #storeform = StoreForm()
            try:
                storeobject = Store.objects.get(businessID=baker.businessID)
                storeform = StoreForm(instance=storeobject)
            except Store.DoesNotExist:
                storeobject=Store()
                storeform = StoreForm(instance=storeobject)
            res_data['store'] = storeform

            return render(request, 'baker/enrollStore2.html', res_data)

    else:
        if request.method == "GET":
            res_data = {}
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'baker/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/')

def opendays(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
        daysobject = OpenDays()
        # dailyobject = DailyAmount()
        if request.method == "POST":
            daysform = OpenDaysForm(request.POST)
            # dailyform = DailyAmountForm(request.POST)
            if daysform.is_valid():
                daysobject.businessID = baker.businessID
                daysobject.monday = daysform.cleaned_data['monday']
                daysobject.tuesday = daysform.cleaned_data['tuesday']
                daysobject.wednesday = daysform.cleaned_data['wednesday']
                daysobject.thursday = daysform.cleaned_data['thursday']
                daysobject.friday = daysform.cleaned_data['friday']
                daysobject.saturday = daysform.cleaned_data['saturday']
                daysobject.sunday = daysform.cleaned_data['sunday']
                daysobject.save()
                res_data['opendays'] = daysform

                setDailyAmounts(baker.businessID,daysobject.sunday,daysobject.monday,daysobject.tuesday,daysobject.wednesday,
                                daysobject.thursday,daysobject.friday,daysobject.saturday)
                return redirect('/baker/manageStore/weekhandle/', res_data)

            else:
                    return redirect('/baker/inappropriateApproach')

        else:
            daysobject = OpenDays.objects.get(businessID=baker.businessID)
            daysform = OpenDaysForm(instance=daysobject)
            res_data['opendays'] = daysform

            # dailyobject = DailyAmount.objects.get(businessID=baker.businessID)
            # dailyform = DailyAmountForm(instance=dailyobject)
            # res_data['dailyform'] = dailyform
            return render(request, 'baker/weekhandle.html', res_data) # 나중에 opendays.html으로 바꿔야함

    else:
        if request.method == "GET":
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'baker/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/')

def dailyamountsetting(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
        # daysobject = OpenDays()
        dailyobject = DailyAmount()
        if request.method == "POST":
            # daysform = OpenDaysForm(request.POST)
            dailyform = DailyAmountForm(request.POST)
            if dailyform.is_valid():
                dailyobject.businessID = baker.businessID
                dailyobject.day1 = dailyform.cleaned_data['day1']
                dailyobject.day2 = dailyform.cleaned_data['day2']
                dailyobject.day3 = dailyform.cleaned_data['day3']
                dailyobject.day4 = dailyform.cleaned_data['day4']
                dailyobject.day5 = dailyform.cleaned_data['day5']
                dailyobject.day6 = dailyform.cleaned_data['day6']
                dailyobject.day7 = dailyform.cleaned_data['day7']
                dailyobject.day8 = dailyform.cleaned_data['day8']
                dailyobject.day9 = dailyform.cleaned_data['day9']
                dailyobject.day10 = dailyform.cleaned_data['day10']
                dailyobject.day11 = dailyform.cleaned_data['day11']
                dailyobject.day12 = dailyform.cleaned_data['day12']
                dailyobject.day13 = dailyform.cleaned_data['day13']
                dailyobject.day14 = dailyform.cleaned_data['day14']
                dailyobject.day15 = dailyform.cleaned_data['day15']
                dailyobject.day16 = dailyform.cleaned_data['day16']
                dailyobject.day17 = dailyform.cleaned_data['day17']
                dailyobject.day18 = dailyform.cleaned_data['day18']
                dailyobject.day19 = dailyform.cleaned_data['day19']
                dailyobject.day20 = dailyform.cleaned_data['day20']
                dailyobject.day21 = dailyform.cleaned_data['day21']
                dailyobject.day22 = dailyform.cleaned_data['day22']
                dailyobject.day23 = dailyform.cleaned_data['day23']
                dailyobject.day24 = dailyform.cleaned_data['day24']
                dailyobject.day25 = dailyform.cleaned_data['day25']
                dailyobject.day26 = dailyform.cleaned_data['day26']
                dailyobject.day27 = dailyform.cleaned_data['day27']
                dailyobject.day28 = dailyform.cleaned_data['day28']
                dailyobject.day29 = dailyform.cleaned_data['day29']
                dailyobject.day30 = dailyform.cleaned_data['day30']
                dailyobject.day31 = dailyform.cleaned_data['day31']
                dailyobject.day32 = dailyform.cleaned_data['day32']
                dailyobject.day33 = dailyform.cleaned_data['day33']
                dailyobject.day34 = dailyform.cleaned_data['day34']
                dailyobject.day35 = dailyform.cleaned_data['day35']
                dailyobject.day36 = dailyform.cleaned_data['day36']
                dailyobject.day37 = dailyform.cleaned_data['day37']
                dailyobject.day38 = dailyform.cleaned_data['day38']
                dailyobject.day39 = dailyform.cleaned_data['day39']
                dailyobject.day40 = dailyform.cleaned_data['day40']
                dailyobject.day41 = dailyform.cleaned_data['day41']
                dailyobject.day42 = dailyform.cleaned_data['day42']
                dailyobject.day43 = dailyform.cleaned_data['day43']
                dailyobject.day44 = dailyform.cleaned_data['day44']
                dailyobject.day45 = dailyform.cleaned_data['day45']
                dailyobject.day46 = dailyform.cleaned_data['day46']
                dailyobject.day47 = dailyform.cleaned_data['day47']
                dailyobject.day48 = dailyform.cleaned_data['day48']
                dailyobject.day49 = dailyform.cleaned_data['day49']
                dailyobject.day50 = dailyform.cleaned_data['day50']
                dailyobject.day51 = dailyform.cleaned_data['day51']
                dailyobject.day52 = dailyform.cleaned_data['day52']
                dailyobject.day53 = dailyform.cleaned_data['day53']
                dailyobject.day54 = dailyform.cleaned_data['day54']
                dailyobject.day55 = dailyform.cleaned_data['day55']
                dailyobject.day56 = dailyform.cleaned_data['day56']
                dailyobject.day57 = dailyform.cleaned_data['day57']
                dailyobject.day58 = dailyform.cleaned_data['day58']
                dailyobject.day59 = dailyform.cleaned_data['day59']
                dailyobject.day60 = dailyform.cleaned_data['day60']
                dailyobject.day61 = dailyform.cleaned_data['day61']
                dailyobject.day62 = dailyform.cleaned_data['day62']

                dailyobject.save()
                res_data['dailyform'] = dailyform

                return redirect('/baker/manageStore/datehandle/', res_data)

            else:
                return redirect('/baker/inappropriateApproach')

        else:
            # daysobject = OpenDays.objects.get(businessID=baker.businessID)
            # daysform = OpenDaysForm(instance=daysobject)
            # res_data['opendays'] = daysform

            # dailyobject = DailyAmount.objects.filter(businessID=baker.businessID)
            try:
                dailyobject = DailyAmount.objects.get(businessID=baker.businessID)
                dailyform = DailyAmountForm(instance=dailyobject)
            except DailyAmount.DoesNotExist:
                dailyobject=DailyAmount()
                dailyform = DailyAmountForm(instance=dailyobject)
            # dailyform = DailyAmountForm()
            res_data['dailyform'] = dailyform
            return render(request, 'baker/dayhandle.html', res_data)  # 나중에 opendays.html으로 바꿔야함

    else:
        if request.method == "GET":
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'baker/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/')

def storeReview(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
    return render(request, 'baker/storeReview.html')

# 케이크 관리
def myCakes(request):
    res_data = {}
    user_id = request.session.get('user')
    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
        #cake_list = Cake.objects.all()
        cake_list = Cake.objects.filter(crn=baker.businessID)
        res_data['cake_list']= cake_list
        return render(request, 'baker/myCakes.html',res_data)
    else:
        if request.method == "GET":
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'baker/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/baker/login')

def cake_add(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
        #cakeobject = Cake()
        if request.method == "POST":
            cakeform = CakeForm(request.POST,request.FILES)
            store = Store.objects.get(pk=baker.businessID)

            if cakeform.is_valid():
                cakeobject = cakeform.save(commit=False)
                cakeobject.crn = store.businessID
                cakeobject.cakeName = cakeform.cleaned_data['cakeName']
                cakeobject.cakeImg = cakeform.cleaned_data['cakeImg']
                cakeobject.cakePrice = cakeform.cleaned_data['cakePrice']
                cakeobject.mini = cakeform.cleaned_data['mini']

                if Cake.objects.filter(cakeName=cakeobject.cakeName, crn=cakeobject.crn).exists():
                    cakeform = CakeForm()
                    res_data['cake'] = cakeform
                    res_data['error'] = "이미 등록된 케이크 이름입니다."
                    return render(request, 'baker/cake_add.html', res_data)
                else:
                    cakeobject.save()
                    # return redirect('/baker/manageCake/myCakes')
                    res_data['cake'] = cakeform
                    # res_data['name'] = cakeobject.cakeImg
                    # return render(request, 'baker/myCakes2.html', res_data)
                    return redirect('/baker/manageCake/myCakes', res_data)


            else:
                    print(cakeform.errors)
                    """cakeform = CakeForm()
                    res_data['cake'] = cakeform
                    res_data['error'] = "이미 등록된 케이크 이름입니다."
                    return render(request, 'baker/cake_add.html', res_data)"""
                    return redirect('/baker/inappropriateApproach')

        else:
            #cakeobject = Cake.objects.get(cakeName=baker.businessID)
            #cakeform = CakeForm(instance=cakeobject)
            cakeform = CakeForm()
            res_data['cake'] = cakeform
            return render(request, 'baker/cake_add.html', res_data)

    else:
        if request.method == "GET":
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'baker/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/')

def cake_edit(request,pk):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
        cakeobject = get_object_or_404(Cake,pk=pk)
        if request.method == "POST":
            cakeform = CakeForm(request.POST,request.FILES,instance=cakeobject)
            #store = Store.objects.get(pk=baker.businessID)

            #try:
            #    cake = Cake.objects.get(cakeName=cakeName)
            if cakeform.is_valid():

                cakeobject = cakeform.save()
                #return redirect('/baker/manageCake/myCakes')
                res_data['cake'] = cakeform
                cakeobject.save()
                res_data['name'] = cakeobject.cakeImg
                #return render(request, 'baker/myCakes.html', res_data)
                return redirect('/baker/manageCake/myCakes', res_data)
            else:
                    print(cakeform.errors)
                    cakeform = CakeForm()
                    res_data['cake'] = cakeform
                    res_data['error'] = "이미 등록된 케이크 이름입니다."
                    return render(request, 'baker/cake_add.html', res_data)
                    #return redirect('/baker/inappropriateApproach')

        else:
            #cakeobject = Cake.objects.get(cakeName=baker.businessID)
            cakeform = CakeForm(instance=cakeobject)
            #cakeform = CakeForm()
            res_data['cake'] = cakeform
            return render(request, 'baker/cake_add.html', res_data)

    else:
        if request.method == "GET":
            res_data = {}
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'baker/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/')


def cake_delete(request,pk):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
        cakeobject = get_object_or_404(Cake, pk=pk)
        cakeobject.delete()
        return redirect('/baker/manageCake/myCakes', res_data)



    else:
        if request.method == "GET":
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'baker/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/')

def options(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
    return render(request, 'baker/options.html')


def manageOrder(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
    return render(request, 'baker/manageOrder.html',res_data)

def mypage(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
    return render(request, 'baker/mypage_baker.html',res_data)

def search(request):
    return render(request, 'baker/idpw_search_baker.html')

def idsearch(request):
    if request.method=="GET":
        return render(request,'baker/idpw_search_baker.html')
    elif request.method == "POST":
        #전송받은 이메일 비밀번호 확인
        email = request.POST.get('email_baker')
        res_data={}
        if Baker.objects.filter(email=email).exists():
            baker = Baker.objects.get(email=email)
            #res_data['searched_id']=baker.userID
            res_data['result']="고객님의 아이디는 "+baker.userID+" 입니다."
            return render(request, 'baker/idpw_search_baker.html',res_data)
            #return redirect('/baker/search', res_data)

        else:
            res_data['result'] = "등록되지 않은 이메일입니다."
            return render(request, 'baker/idpw_search_baker.html',res_data)
            #return redirect('/baker/search', res_data)

def pwsearch(request):
        print("here")
        userid = request.POST.get('userid')
        print(userid)
        res_data = {}
        if Baker.objects.filter(userID=userid).exists():
            baker = Baker.objects.get(userID=userid)
            temppw = passwordMaker()
            current_site = get_current_site(request)
            message = passwordMessage(current_site.domain,userid,temppw)
            baker.password = make_password(temppw)
            baker.save()
            mail_subject = "[The Cake] 임시 비밀번호 전송"
            user_email = baker.email
            email = EmailMessage(mail_subject, message, to=[user_email])
            email.send()
            res_data['comment'] = user_email + " 로 임시 비밀번호가 전송되었습니다."
            #return redirect('/baker/search', res_data)
            return render(request, 'baker/idpw_search_baker.html',res_data)

        else:
            res_data['comment'] = "등록되지 않은 아이디입니다."
            #return redirect('/baker/search', res_data)
            return render(request, 'baker/idpw_search_baker.html',res_data)

def pwsearch1(request):
    """if request.method=="GET":
        print("here")
        return render(request,'baker/idpw_search_baker.html')
    elif request.method == "POST":
        print("posting")

        userid = request.POST.get('userid')
        res_data = {}
        if Baker.objects.filter(userID=userid).exists():
            baker = Baker.objects.get(userID=userid)
            temppw = passwordMaker()
            current_site = get_current_site(request)
            message = passwordMessage(current_site.domain,userid,temppw)
            baker.password = temppw
            baker.save()
            mail_subject = "[The Cake] 임시 비밀번호 전송"
            user_email = baker.email
            email = EmailMessage(mail_subject, message, to=[user_email])
            email.send()
            res_data['comment'] = user_email + " 로 임시 비밀번호가 전송되었습니다."
            return redirect('/baker/search', res_data)
            #return render(request, 'baker/idpw_search_baker.html',res_data)

        else:
            res_data['comment'] = "등록되지 않은 아이디입니다."
            return redirect('/baker/search', res_data)
            #return render(request, 'baker/idpw_search_baker.html',res_data)
"""


def editInfo(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
    return render(request,'baker/editMyInfo.html',res_data)

def changeAccountInfo(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name
        # bakerobject = Baker()
        if request.method == 'POST':
            bakerform = BakerForm(request.POST)
            if bakerform.is_valid():  # 유효성 검사

                # userID = bakerform.cleaned_data['userID'],
                # email = bakerform.cleaned_data['email'],
                baker.name = bakerform.cleaned_data['name']
                baker.phoneNum = bakerform.cleaned_data['phoneNum']
                baker.password = make_password(request.POST.get('password_baker',None))

                baker.save()
                res_data['baker'] = bakerform
                # res_data['name'] = storeobject.storeImg
                return render(request, 'baker/editMyInfo.html', res_data)
            else:
                return redirect('/baker/inappropriateApproach')

        else:
            baker = Baker.objects.get(businessID=baker.businessID)
            bakerform = BakerForm(instance=baker)
            # storeform = StoreForm()
            res_data['baker'] = bakerform

            return render(request, 'baker/editMyInfo.html', res_data)

    else:
        if request.method == "GET":
            res_data = {}
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'baker/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/')

def checkPw(request):
    res_data = {}
    user_id = request.session.get('user')
    if user_id:
        baker = Baker.objects.get(pk=user_id)
        res_data['bakername'] = baker.name

        if request.method == "GET":
            return render(request, 'baker/checkPw.html')
        elif request.method == "POST":
            if baker.password == request.POST.get('password'):
                return redirect('/baker/myPage/editMyInfo/',res_data)
            else:
                res_data['error'] = "비밀번호가 틀렸습니다."
                return render(request,'baker/checkPw.html',res_data)


    else:
        if request.method == "GET":
            res_data['comment'] = "잘못된 접근입니다. 로그인을 해주세요!"
            return render(request, 'baker/inappropriateApproach.html', res_data)
        elif request.method == "POST":
            return redirect('/')

def logout(request):
    res_data = {}

    if request.method == "GET":
        if request.session['user']:
            user_id = request.session.get('user')
            baker = Baker.objects.get(pk=user_id)
            del (request.session['user'])
            res_data['comment'] = baker.name + " 님의 계정이 성공적으로 로그아웃되었습니다!"
            return render(request, 'baker/logout_baker.html', res_data)
        else:
            return redirect('/baker/inappropriateApproach')
    elif request.method == "POST":
        return redirect('/')

