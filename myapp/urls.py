from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('menu/',views.menu),
    path('postproperty/',views.form_view),
    path('hello/',views.hello_user),
    path('signup/',views.user_sign_up,name="signup_page"),
    path('login/',views.user_login_page,name="loginpage"),
]