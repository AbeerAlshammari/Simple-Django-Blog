from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('users/', views.users_page, name='users'),
    path('blogs/', views.blogs_page, name='blogs'),
    path('comments/', views.comments_page, name='comments'),
    path('categories/', views.categories_page, name='categories'),
    path('blog/<int:post_id>/', views.blog_details, name='blog_details'),
]