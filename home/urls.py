from django.urls import path
#from django.contrib import admin

from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    #path('admin/',admin.site.urls),
    #path('',include('enrollStore.urls')),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)