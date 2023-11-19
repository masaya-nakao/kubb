from django.urls import path
from . import views

app_name='dream'

urlpatterns = [
    path('', views.index, name='index'),
    path('preference_list/', views.preference_list, name='preference_list'),
    path('agenda_list/', views.agenda_list, name='agenda_list'),
    path('recruitment_list/', views.recruitment_list, name='recruitment_list'),
    path('preference_create/', views.preference_create, name='preference_create'),
    #path('preference_create/', PreferenceCreateView.as_view(), name='preference_create'),
    path('agenda_create/', views.agenda_create, name='agenda_create'),
    path('recruitment_create/', views.recruitment_create, name='recruitment_create'),
    path('<str:title>/detail/', views.detail, name='detail'),
    path('<str:title>/delete/', views.delete, name='delete'),
    #path('preference_search', PreferenceSearchView.as_view(), name='preference_search'),
    path('preference_search', views.preference_search, name='preference_search'),
    path('agenda_search', views.agenda_search, name='agenda_search'),
    path('recruitment_search', views.recruitment_search, name='recruitment_search'),
    path('preference_groupchat/<str:room_name>', views.preference_groupchat, name='preference_groupchat'),
    path('<str:room_name>/agenda_groupchat/', views.agenda_groupchat, name='agenda_groupchat'),
    path('<str:room_name>/preference_like/', views.preference_like, name='preference_like'),
    path('<str:room_name>/agenda_like/', views.agenda_like, name='agenda_like'),
    path('<str:room_name>/recruitment_like/', views.recruitment_like, name='recruitment_like'),
    path('<int:id>/preference_like_delete/', views.preference_like_delete, name='preference_like_delete'),
    path('<int:id>/agenda_like_delete/', views.agenda_like_delete, name='agenda_like_delete'),
    path('<int:id>/recruitment_like_delete/', views.recruitment_like_delete, name='recruitment_like_delete'),
    #path('<str:room_name>/profile/', views.profile, name='profile'),
    path('introduction/',views.introduction_view,name='introduction'),
]