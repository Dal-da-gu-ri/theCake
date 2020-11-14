from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # 로그인, 아이디비번찾기, 회원가입
    path('login/', views.login, name='login_customer'),
    # path('idpw_search/', views.idpw_search, name='idpw_search_customer'),
    #path('signUp/', views.signUp, name='signUp_customer'),
    path('signUp/idCheck/', views.useridCheck, name='idCheck'),
    path('signUp/join/', views.join, name='join_customer'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
    path('inappropriateApproach/',views.wrongApproach,name='wrongApproach'),
    path('logout/', views.logout, name='logout_customer'),

    path('main/', views.main_customer, name='main_customer'),
    path('main/stores/',views.showStores,name='showStores'),
    path('main/stores/<int:pk>/', views.storeInfo, name='storeInfo'),
    # path('main/stores/<int:pk>/<int:pk1>/order', views.cakeOrder, name='cakeOrder'),
    path('main/stores/<int:crn>/order/<int:cakepk>/', views.cakeOrder, name='cakeOrder'),
    # path('main/stores/<int:pk1>/', views.cakeOrder, name='cakeOrder'),

    path('temp/', views.temp, name='temp'),
    # path('main/showStores2', views.showStores2, name='showStores2'),

    # 주문하기
    # 화면에서 위치, 수령일 바꾸고 싶으면 url 바뀌어야..(?)
    # 메인화면(위치, 수령일 선택 화면)
    # path('order/', views.searchStoreList, name='searchStorelist_customer'),
    # # 가게목록 보여주는 화면.
    # # (수령일, 위치(다시 선택 가능?), 분류기준<맛별점, 서비스별점, 디자인별점, 종합별점>, 매장명검색, 매장목록<매장명, 매장위치, 전화번호, 종합별점>)
    # path('order/matchedStoreList', views.storeList, name='matchedStoreList_customer'),
    # # 가게 선택 후, 그 가게의 케이크 목록 보여주는 화면.
    # # (매장명, 주문가능한 날짜 (달력), 매장소개글, 수령일(다시 선택 가능?), 픽업시간, 케이크목록<케이크 사진, 케이크 이름, 케이크 최소금액, 미니사이즈가능여부>)
    # path('order/selectedStoreCakeList', views.cakeList, name='selectedStoreCakeList_customer'),
    # # 가게의 케이크 목록 보여주는 화면에서 가게명을 선택했을 때 보이는 가게의 정보
    # # (영업시간, 전화번호,,이 정도면 되나?)
    # path('order/selectedStoreCakeList/storeInfo', views.storeInfo, name='storeInfo_customer'),
    # # 나만의 케이크
    # # (선택한 케이크 사진, 옵션 선택<필수옵션, 선택옵션<선택지, 가격>>, 사장님이 전하는 말, 색조합)
    # path('order/selectedCake', views.selectedCake, name='selectedCake_customer'),
    # # 색조합 선택할 때마다 다른 url인가? 색조합선택화면은 다를 듯
    # path('order/selectedCake/backgroundColor', views.backgroundColor, name='backgroundColor_customer'),
    # path('order/selectedCake/textColor', views.textColor, name='textColor_customer'),
    # path('order/selectedCake/creamColor', views.creamColor, name='creamColor_customer'),

    # 주문내역조회
    # (수령날짜, 수령시간, 선택한 케이크 이미지, 최종가격, 주문매장, 주문진행상황, 주문번호(?))
    path('orderList/', views.orderlist, name='orderList_customer'),
    # 주문내역조회-수정하기는 selectedCake과 다른 페이지라고 해야하나 아니면 그 화면에 그대로 + 정보 자동기입?
    # path('orderList/changeOrder', views.changeOrder, name='changeOrder_customer'),

    # 마이페이지
    # path('myPage/editMyInfo/',views.changeAccountInfo,name='editInfo'),
    path('myPage/editMyInfo/checkPw', views.checkPw, name='checkPw'),
    path('myPage/editMyInfo/changePw', views.changePw, name='changePw'),
    # path('mypage/', views.mypage, name='mypage_customer'),
    path('inappropriateApproach/', views.wrongApproach, name='wrongApproach')

]
