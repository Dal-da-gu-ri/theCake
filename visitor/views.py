from django.shortcuts import render
from home.models import *
from baker.forms import *
from customer.forms import *
from customer.mappingdate import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def visitorlogin(request):
    if request.method=="GET":
        return redirect('/')


def main_visitor(request):
    res_data = {}
    if request.method == 'GET':
        return render(request, 'visitor/main_visitor.html', res_data)
    elif request.method == 'POST':
        request.session['sido'] = request.POST.get('sido', None)
        request.session['sigungu'] = request.POST.get('sigungu', None)
        request.session['dong'] = request.POST.get('dong', None)
        return redirect('/visitor/main/stores', res_data)

def showStores(request):
    res_data = {}
    sido = request.GET['sido']
    sigugun = request.GET['sigugun']
    dong = request.GET['dong']
    day = request.GET['date']
    res_data = {'sido': sido, 'sigugun': sigugun, 'dong': dong, 'date': day}
    orderdate = request.GET['date']
    store_list = []
    isStore = False

    review_list = Review.objects.all().order_by('cakeName')
    res_data['review_list'] = review_list

    if day:
        orderyear = int(orderdate[0]) * 1000 + int(orderdate[1]) * 100 + int(orderdate[2]) * 10 + int(orderdate[3])
        ordermonth = int(orderdate[5]) * 10 + int(orderdate[6])
        orderday = int(orderdate[8]) * 10 + int(orderdate[9])
        request.session['selectedYear'] = orderyear
        request.session['selectedMonth'] = ordermonth
        request.session['selectedDay'] = orderday

        if sido:
            if sigugun:
                if dong:
                    stores = Store.objects.filter(daum_sido=sido, daum_sigungu=sigugun, daum_dong=dong)
                    for store in stores:
                        if mappingDate(store, ordermonth, orderday) == True:  # 주문가능한 수량이 있을경우
                            storeobject = Store.objects.get(businessID=store)
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
                        if mappingDate(store, ordermonth, orderday) == True:  # 주문가능한 수량이 있을경우
                            storeobject = Store.objects.get(businessID=store)
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

                if isStore == True:
                    res_data['happy'] = "조회된 가게 있음."
                else:
                    res_data['error'] = "조회된 가게가 없습니다."

        else:
            res_data['error'] = "픽업 위치를 선택해주세요."



    else:  # 선택된 가게가 없는 데 넘어온 경우..
        res_data['error'] = "날짜를 선택해주세요."
        # return HttpResponse(user_id)

    res_data['store_list'] = store_list
    return render(request, 'visitor/stores.html', res_data)


def storeInfo(request,pk):
    res_data = {}
    storeobject = get_object_or_404(Store, pk=pk)

    if request.method == "GET":
        storeform = StoreForm(instance=storeobject)
        # cakeform = CakeForm()
        res_data['store'] = storeform

        store_list = Store.objects.filter(pk=pk)
        res_data['store_list'] = store_list
        cake_list = Cake.objects.filter(crn=storeobject.businessID)
        res_data['cake_list'] = cake_list
        res_data['selectedYear'] = request.session.get('selectedYear')
        res_data['selectedMonth'] = request.session.get('selectedMonth')
        res_data['selectedDay'] = request.session.get('selectedDay')

        return render(request, 'visitor/showCakes.html', res_data)

def showReview(request, pk):
    res_data = {}
    store = Store.objects.get(businessID=pk)
    review_list = Review.objects.filter(storeInfo=pk).order_by('cakeName')
    res_data['store'] = store
    res_data['review_list'] = review_list
    return render(request, 'visitor/showReview.html', res_data)