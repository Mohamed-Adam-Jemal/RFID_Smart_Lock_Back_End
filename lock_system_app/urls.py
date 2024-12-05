from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('get-users/', views.get_users, name='get_users'),
    path('add-user/', views.add_user, name='add_user'),
    path('update-user/', views.update_user, name='update_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add-access-log/', views.add_access_log, name='add_access_log'),
    path('get-access-log/', views.get_access_log, name='get_access_log'),

]
