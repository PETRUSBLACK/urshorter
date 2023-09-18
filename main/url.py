from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UrlDataViewSets
)

app_name = "user"
router = DefaultRouter()
router.register("prices", UrlDataViewSets)

urlpatterns = [
    path("", include(router.urls)),
]
