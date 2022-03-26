from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from api.views import SpreadSheetViewSet

router = routers.DefaultRouter()
router.register('spreadsheets', SpreadSheetViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
