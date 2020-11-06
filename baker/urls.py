from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login_baker'),
    path('search/', views.search, name='search_baker'),
    path('search/id', views.idsearch, name='id'),
    path('search/pw', views.pwsearch, name='pw'),
    path('signUp/crnCheck/', views.crnCheck, name='crnCheck'),
    path('signUp/join/', views.join, name='join_baker'),

    path('signUp/join/idcheck/',views.isID,name='isID_baker'),
    path('signUp/join/emailcheck/', views.isEmail, name='isEmail_baker'),
    path('signUp/join/crncheck/', views.isCRN, name='isCRN_baker'),

    # 마이페이지
    path('myPage/editMyInfo', ),
    path('myPage/changePw', ),


    #path('signUp/join/emailSent/',views.join, name='emailSent_baker'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
    path('inappropriateApproach/',views.wrongApproach,name='wrongApproach'),
    path('logout/',views.logout, name='logout_baker'),
    # 가게 관리
    path('manageStore/enrollStore/', views.enrollStore, name='enrollStore_baker'),
    path('manageStore/opendays/', views.opendays, name='opendays_baker'),
    path('manageStore/storeReview/', views.storeReview, name='storeReview_baker'),
    path('temp/', views.temp, name='temp'),
    # 케이크 관리
    path('manageCake/myCakes/', views.myCakes, name='myCakes_baker'),
    # 하나의 케이크에 해당하는 정보를 불러오는 path도 있어야함.(뷰 함수는 id같은 pk로 정보가져오는 함수)
    path('manageCake/myCakes/cakeAdd/', views.cake_add, name='cake_add'),
    path('manageCake/myCakes/cakeEdit/<int:pk>/', views.cake_edit, name='cake_edit'),
    path('manageCake/options/', views.options, name='options_baker'),
    path('manageCake/myCakes/cakeEdit/<int:pk>/delete', views.cake_delete, name='cake_delete'),

    # 주문 관리
    path('manageOrder/', views.manageOrder, name='manageOrder_baker'),

    path('mypage/', views.mypage, name='mypage_baker')
]
