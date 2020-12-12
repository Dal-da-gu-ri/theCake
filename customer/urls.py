from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # 로그인, 아이디비번찾기, 회원가입
    path('login/', views.login, name='login_customer'),

    path('search/', views.search, name='search_customer'),
    path('search/id', views.idsearch, name='id'),
    path('search/pw', views.pwsearch, name='pw'),

    path('signUp/idCheck/', views.useridCheck, name='idCheck'),
    path('signUp/join/', views.join, name='join_customer'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
    path('inappropriateApproach/',views.wrongApproach,name='wrongApproach'),
    path('logout/', views.logout, name='logout_customer'),

    # 주문하기
    path('main/', views.main_customer, name='main_customer'),
    path('main/stores/',views.showStores,name='showStores'),
    path('main/stores/<int:pk>/', views.storeInfo, name='storeInfo'),
    path('main/stores/<int:pk>/showReview', views.showReview, name='showReview'),
    path('main/stores/<int:crn>/order/<str:cakepk>/', views.cakeOrder, name='cakeOrder'),

    # 주문내역조회
    path('orderList/', views.orderlist, name='orderList_customer'),
    path('orderList/<int:orderNum>/pay', views.cakePay, name='pay'),
    path('orderList/<int:orderNum>/paySuccess', views.paySuccess, name='paySuccess'),
    path('orderList/<int:orderNum>/review', views.writeReview, name='writeReview'),
    path('orderList/<str:pk>/delete', views.order_delete, name='order_delete'),

    # 마이페이지
    path('myPage/editMyInfo/checkPw', views.checkPw, name='checkPw'),
    path('myPage/editMyInfo/changePw', views.changePw, name='changePw'),
    path('myPage/deleteAccount', views.deleteAccount, name='deleteAccount'),
    path('myPage/deleteAccount/bye/', views.bye, name='bye'),

    path('inappropriateApproach/', views.wrongApproach, name='wrongApproach')

]
