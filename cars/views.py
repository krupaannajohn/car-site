from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from carSite.settings import BASE_DIR
# Create your views here.

def index(request):
    # cars_data.objects.all().delete() #To Delete the data
    cars = cars_data.objects.all()
    return render(request, 'index.html', {'cars':cars, 'BASE_DIR':BASE_DIR})


def admin1(request):
    if request.method == 'POST':
        car = cars_data()
        car.car_Name = request.POST.get("car_name", False)
        car.car_Price = request.POST.get("car_price", False)
        car.Car_Model = request.POST.get("car_model", False)
        car.car_Photo = request.FILES.get("car_photo", False)
        car.save()

    
    return render(request, 'upload.html')


def delete_car(request, car_id):
    # Get the car object to delete
    car = get_object_or_404(cars_data, pk=car_id)
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Delete the car object
        car.delete()
        # Redirect to the index page after deletion
        return redirect('cars:index')
    
    # If the request method is not POST, render a confirmation page
    return render(request, 'delete_car.html', {'car': car})
