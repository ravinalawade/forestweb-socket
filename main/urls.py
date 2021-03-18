from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path('test_api', views.Test_api.as_view(), name='test_api'),
]