from django.urls import path
from users import views

app_name = "users_urls"

urlpatterns = [
    path('sign-in/', views.login, name="signin_url"),
    path('sign-up/', views.signup, name="signup_url"),
    path('logout/', views.logout_user, name="logout_url"),

    path('create-profile/', views.create_birthday_profile, name="create_profile_url"),
    path('delete-profile/<pk>/', views.delete_profile, name="delete_profile"),
    path('edit-profile/<pk>/', views.edit_birthday_profile, name="edit_profile"),

]