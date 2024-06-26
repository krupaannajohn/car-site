from django.urls import path

from . import views

app_name='cars'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.admin1, name='upload'),
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),
]
