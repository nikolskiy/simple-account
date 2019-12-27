from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('ping/', views.ping),
    path('add/', views.add_view),
    path('subtract/', views.subtract_view),
    path('status/', views.status_view),
    path('internal/rebalance/', views.rebalance)
]
