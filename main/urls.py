from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login_view,name="login"),
    path('logout/', views.logout_user, name='logout'),
]
