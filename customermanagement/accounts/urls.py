from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('employee/<str:pk>',views.employee,name='employee'),
    path('works/',views.works,name='works'),
]
