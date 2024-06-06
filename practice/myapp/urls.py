from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PromotionViewSet
router = DefaultRouter()
router.register(r"promotions", PromotionViewSet)
urlpatterns = [
    path("", views.home, name="home"),
    path("orders/", views.order, name="orders"),
    path("api/", include(router.urls)),
]