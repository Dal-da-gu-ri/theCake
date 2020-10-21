from django.shortcuts import render, redirect
from home.models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake, checkBaker
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from .crn import Search_CRN

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
        businessName = request.POST.get('businessName',None)
        namebaker = request.POST.get('name_baker',None)
        emailbaker = request.POST.get('email_baker',None)
        passwordbaker = request.POST.get('password_baker',None)
        phoneNumbaker = request.POST.get('phoneNum_baker',None)
        res_data = {}
        try:
            curBaker = checkBaker.objects.get(businessname = businessName)
            crnNum = curBaker.businessCRN
            baker = Baker(
                businessID=crnNum,
                businessName=businessName,
                email=emailbaker,
                name=namebaker,
                phoneNum=phoneNumbaker,
                password=make_password(passwordbaker)
            )
            baker.save()
            return redirect('/baker/login')
            #return render(request, 'fuser/login.html')
        except checkBaker.DoesNotExist:
            # comment = None
            res_data['error'] = "등록되지 않은 사업자명입니다."
            return render(request, 'baker/join_baker.html', res_data)


def login(request):
    if request.method=="GET":
        return render(request,'baker/login_baker.html')
    elif request.method == "POST":
        #전송받은 이메일 비밀번호 확인
        businessID = request.POST.get('businessID')
        password = request.POST.get('password')

        #유효성 처리
        res_data={}
        if Baker.objects.filter(businessID=businessID).exists():
            baker = Baker.objects.get(businessID=businessID)
            if check_password(password,baker.password):
                #응답 데이터 세션에 값 추가. 수신측 쿠키에 저장됨
                request.session['user']=baker.businessID

                #리다이렉트
                #return redirect('/') #urls에 정의해둔 home으로
                return render(request,'baker/enrollStore.html')
            else:
                res_data['error'] = "비밀번호가 틀렸습니다."
                return render(request, 'baker/login_baker.html', res_data)

        else:
            res_data['error'] = "존재하지 않는 사업자번호입니다."
            return render(request,'baker/login_baker.html',res_data)

def crnCheck(request):
    if request.method == "GET":  # url을 이용한 방법
        return render(request, 'baker/crnCheck.html')
    elif request.method == "POST":  # 등록 버튼을 사용한 방법기
        businessName = request.POST.get('businessName',None)
        crn = request.POST.get('businessID', None)
        res_data = {}
        if Search_CRN(crn) == "부가가치세 일반과세자 입니다.":
            try:
                baker = checkBaker.objects.get(businessCRN = crn)
                res_data['error'] = "이미 등록된 사업자등록번호입니다."
                return render(request, 'baker/crnCheck.html', res_data)
            except checkBaker.DoesNotExist:
                #comment = None
                checkbaker = checkBaker(
                    businessname=businessName,
                    businessCRN=crn
                )
                checkbaker.save()
                return redirect('/baker/signUp/join')
                #return render(request, 'baker/join_baker.html')


        else:
            res_data['error'] = "유효하지 않은 사업자등록번호입니다."
            return render(request, 'baker/crnCheck.html', res_data)

def idpw_search(request):
    return render(request, 'baker/idpw_search_baker.html')

def valid(request): #사업자번호확인 -> join
    return HttpResponse("Valid page!")






# 가게 관리
def enrollStore(request):
    if request.method == "GET":
        return render(request, 'baker/enrollStore.html')
    elif request.method == "POST":
        businessID = request.session.get('user')
        if businessID:
            baker = Baker.objects.get(pk=businessID)

            storeName = request.POST.get('storeName',None)
            storeContact = request.POST.get('storeContact',None)
            pickopen = request.POST.get('pickUpOpen',None)
            pickclose = request.POST.get('pickUpClose',None)
            aboutstore = request.POST.get('aboutStore',None)

            try:
                store = Store.objects.get(pk = businessID)
                store.storeName = storeName
                store.storeContact = storeContact
                store.pickUpOpen = pickopen
                store.pickUpClose = pickclose
                store.aboutStore = aboutstore
                store.save()
                return render(request, 'baker/enrollStore.html')
            except checkBaker.DoesNotExist:
                #comment = None
                store = Store(
                    businessID = businessID,
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
