from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.main_visitor, name='main_visitor'),
    path('main/stores/',views.showStores,name='showStores'),
    path('main/stores/<int:pk>/', views.storeInfo, name='storeInfo'),
    path('main/stores/<int:pk>/showReview', views.showReview, name='showReview'),
    path('main/stores/<int:crn>/order/<str:cakepk>/', views.cakeOrder, name='cakeOrder'),
    path('login/',views.visitorlogin, name='visitorlogin')
    ]