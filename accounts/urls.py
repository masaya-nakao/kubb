from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    # 他のパターン
    path('login/',views.login_view, name='login'),
    path('terms/',views.terms_view,name='terms'),
]
