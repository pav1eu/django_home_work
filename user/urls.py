from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from user.views import RegisterView

app_name = 'user'

urlpatterns = [
    path("login/", LoginView.as_view(template_name='user/login.html'), name="login"),
    path("logout/", LogoutView.as_view(next_page='catalog:products_list'), name="logout"),
    path('register/', RegisterView.as_view(template_name='user/user_form.html'), name='register'),
]