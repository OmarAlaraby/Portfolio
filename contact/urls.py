from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('send/', views.save_contact_message, name='send_message'),
] 