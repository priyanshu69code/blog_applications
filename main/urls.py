from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login_view,name="login"),
    path('logout/', views.logout_user, name='logout'),
    path('create/',views.create_blog,name='create'),
    path('post/<int:blog_id>/', views.view_blog_post, name='view_blog_post'),
    path('user_posts/', views.user_posts, name='user_posts'),
    path('delete_post/<int:blog_id>/', views.delete_post, name='delete_post'),
    path('edit_post/<int:blog_id>/', views.edit_post, name='edit_post'),
]
