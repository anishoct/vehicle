from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm


def car(request):
    car=Car.objects.all()
    context={
        'car_list':car
    }
    return render(request,'car.html',context)

def detail(request,car_id):
    car=Car.objects.get(id=car_id)
    return render(request,'detail.html', {'car':car})
def add_car(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        car=Car(name=name,desc=desc,year=year,img=img)
        car.save()
    return render(request,'add.html')
def update(request,id):
    car=Car.objects.get(id=id)
    form=CarForm(request.POST or None,request.FILES,instance=car)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'car':car})

def delete(request,id):
    if request.method== 'POST':
        car=Car.objects.get(id=id)
        car.delete()
        return redirect('/')
    return render(request,'delete.html')





# Create your views here.
