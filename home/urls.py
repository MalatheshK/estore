from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home_page'),
    path('buy', views.buy, name = 'buy_page'),
    path('about_us', views.about, name= 'about_us' )
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)