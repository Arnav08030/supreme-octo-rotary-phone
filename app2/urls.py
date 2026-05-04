from django.urls import path
from . import views
urlpatterns=[
    path('data/', views.data, name='data'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('update/',views.update, name='update'),
    path('get_states/', views.get_states, name='get_states'),
    path('get_districts/', views.get_districts, name='get_districts'),
    path('input_passwords/', views.input_passwords, name='input_passwords')

]