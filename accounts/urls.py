from django.contrib.auth.views import LoginView
from django.urls import path
from .views import login_view,terms_view,introduction_view

app_name='accounts'

urlpatterns = [
    # 他のパターン
    path('login/',login_view, name='login'),
    path('terms/',terms_view,name='terms'),
    path('introduction/',introduction_view,name='introduction'),
    # 他のパター
]


