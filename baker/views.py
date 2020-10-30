from django.shortcuts import render, redirect, get_object_or_404
from home.models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake, checkBaker
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from .crn import Search_CRN
import json
from home.tokens import account_activation_token
from .textBaker import messageSend
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_text
from .forms import CakeForm
#make_password(str) : 이 함수에 넣어준 문자열을 암호화합니다. (hashing)
#check_password(a,b) : a,b가 일치하는지 확인, 반환합니다.

################################
# 이메일 인증 백엔드 구역이래요!!!! #
################################

from django.http import HttpResponse, JsonResponse
# Create your views here.

def join(request):
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
        #return HttpResponse('비정상적인 접근입니다.')

def wrongApproach(request):
    if request.method == "GET":
        res_data = {}
        res_data['comment'] = "잘못된 접근입니다."
        return render(request, 'baker/inappropriateApproach.html',res_data)
    elif request.method == "POST":
        return redirect('/')

def idpw_search(request):
    return render(request, 'baker/idpw_search_baker.html')

def valid(request): #사업자번호확인 -> join
    return HttpResponse("Valid page!")






# 가게 관리
def enrollStore(request):
    res_data = {}
    user_id = request.session.get('user')

    if user_id:
        baker = Baker.objects.get(pk=user_id)
        #return HttpResponse(baker.name)

        if request.method == "GET":
            res_data['user.baker.name'] = baker.name
            return render(request, 'baker/enrollStore.html')

        elif request.method == "POST":

            businessID = baker.businessID
            storeName = request.POST.get('storeName', None)
            storeContact = request.POST.get('storeContact', None)
            pickopen = request.POST.get('pickUpOpen', None)
            pickclose = request.POST.get('pickUpClose', None)
            aboutstore = request.POST.get('aboutStore', None)

            try:
                store = Store.objects.get(pk=businessID)
                store.storeName = storeName
                store.storeContact = storeContact
                store.pickUpOpen = pickopen
                store.pickUpClose = pickclose
                store.aboutStore = aboutstore
                store.save()
                return render(request, 'baker/enrollStore.html')
            except checkBaker.DoesNotExist:
                # comment = None
                store = Store(
                    businessID=businessID,
                    storeName=storeName,
                    storeContact=storeContact,
                    pickUpOpen=pickopen,
                    pickUpClose=pickclose,
                    aboutStore=aboutstore
                    # storeImg
                    # location
                    # manager
                )
                store.save()
                return render(request, 'baker/enrollStore.html')
            # businessID = request.session.get('user')
            # if businessID:
            #     baker = Baker.objects.get(pk=businessID)
            #
            #     storeName = request.POST.get('storeName',None)
            #     storeContact = request.POST.get('storeContact',None)
            #     pickopen = request.POST.get('pickUpOpen',None)
            #     pickclose = request.POST.get('pickUpClose',None)
            #     aboutstore = request.POST.get('aboutStore',None)
            #
            #     try:
            #         store = Store.objects.get(pk = businessID)
            #         store.storeName = storeName
            #         store.storeContact = storeContact
            #         store.pickUpOpen = pickopen
            #         store.pickUpClose = pickclose
            #         store.aboutStore = aboutstore
            #         store.save()
            #         return render(request, 'baker/enrollStore.html')
            #     except checkBaker.DoesNotExist:
            #         #comment = None
            #         store = Store(
            #             businessID = businessID,
            #             storeName=storeName,
            #             storeContact=storeContact,
            #             pickUpOpen=pickopen,
            #             pickUpClose=pickclose,
            #             aboutStore=aboutstore
            #             # storeImg
            #             # location
            #             # manager
            #         )
            #         store.save()
            #         return render(request, 'baker/enrollStore.html')

                # return render(request, 'baker/enrollStore.html')
    else:
        return redirect('/baker/inappropriateApproach')

def opendays(request):
    return render(request, 'baker/opendays.html')
def storeReview(request):
    return render(request, 'baker/storeReview.html')

# 케이크 관리
def myCakes(request):

    return render(request, 'baker/myCakes.html')

def cake_create(request):
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.ip = request.META['REMOTE_ADDR']
            cake.save()
            return redirect('/baker/manageCake/myCakes')
    else:
        form = CakeForm()
    context = {
        'form': form
    }
    return render(request, 'baker/cake_create.html', context)

def options(request):
    return render(request, 'baker/options.html')


def manageOrder(request):
    return render(request, 'baker/manageOrder.html')

def mypage(request):
    return render(request, 'baker/mypage_baker.html')


def logout(request):
    if request.method == "POST":
        if request.session['user']:
            del(request.session['user'])
            return redirect('/baker/login')
        return redirect('/')