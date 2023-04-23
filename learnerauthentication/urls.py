from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name="home"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('test/', views.test, name="test"),
    path('home/new_parcel/', views.new_parcel, name="new_parcel"),

]