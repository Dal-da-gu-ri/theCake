from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login_baker'),
    path('idpw_search/', views.idpw_search, name='idpw_search_baker'),
    path('signUp/crnCheck/', views.crnCheck, name='crnCheck'),
    path('signUp/join/', views.join, name='join_baker'),
    #path('signUp/join/emailSent/',views.join, name='emailSent_baker'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
    path('inappropriateApproach/',views.wrongApproach,name='wrongApproach'),
    path('logout/',views.logout, name='logout_baker'),
    # 가게 관리
    path('manageStore/enrollStore/', views.enrollStore, name='enrollStore_baker'),
    path('manageStore/opendays/', views.opendays, name='opendays_baker'),
    path('manageStore/storeReview/', views.storeReview, name='storeReview_baker'),

    # 케이크 관리
    path('manageCake/myCakes/', views.myCakes, name='myCakes_baker'),
    # 하나의 케이크에 해당하는 정보를 불러오는 path도 있어야함.(뷰 함수는 id같은 pk로 정보가져오는 함수)
    path('manageCake/myCakes/cakeAdd/', views.cake_create, name='cake_add'),
    path('manageCake/options/', views.options, name='options_baker'),

    # 주문 관리
    path('manageOrder/', views.manageOrder, name='manageOrder_baker'),

    path('mypage/', views.mypage, name='mypage_baker')
]
