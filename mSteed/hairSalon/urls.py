from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:day>/<str:hour>', views.make_appointment, name='make_appointment')
]
