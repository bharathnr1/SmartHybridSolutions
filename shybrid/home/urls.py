from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('ajax/send_email/', views.send_email, name='send_email'),
]