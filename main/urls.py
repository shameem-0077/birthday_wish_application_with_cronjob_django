from django.urls import path
from main import views

app_name = "main_urls"

urlpatterns = [
    path('', views.home, name="home_url"),
]