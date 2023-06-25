from django.urls import path
from django.contrib.auth import views as auth_view

from .views import signup, mypage

app_name = 'user'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('mypage/<int:user_id>/', mypage, name='mypage'),
]
