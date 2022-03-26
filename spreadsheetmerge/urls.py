from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from api import views
from api.views import merge_two_spreadsheets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', obtain_auth_token),
    path('merge_two_spreadsheets/', merge_two_spreadsheets),
]
