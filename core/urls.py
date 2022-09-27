from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name='main'), # 메인홈

    # path('mypage/', views.mypage, name='mypage'), #마이페이지

    path('resigter/', views.resigter, name='resigter'), # 회원가입
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #로그인
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #로그아웃
]