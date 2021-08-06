from django.urls import path
from .views import*
from django.contrib.auth import views as auth_view
urlpatterns=[
    path('register/',register,name="user-register"),
    path('login/',auth_view.LoginView.as_view(template_name='user/login.html',extra_context={'title':"Login"}),name="user-login"),
    path('logout/',auth_view.LogoutView.as_view(template_name='user/logout.html',extra_context={'title':"Logout"}),name="user-logout")
]