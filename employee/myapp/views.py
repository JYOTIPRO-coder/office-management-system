from django.shortcuts import render,redirect
from .models import Employee,Role,Department
from .forms import Addrecordform,updaterecordform

def index(request):
    return render(request,'index.html')

def add_emp(request):
    form=Addrecordform()
    if request.method=="POST":
        form=Addrecordform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-emp')
    context={'forms':form}
    return render(request,'add_emp.html',context=context)

def del_emp(request,pk):
    
    return render(request,'del_emp.html')

def view_emp(request):
    employee=Employee.objects.all()
    context={'employees':employee}
    
    return render(request,'view_emp.html',context=context)


def update_emp(request):
    employee=Employee.objects.all()
    context={'employees':employee}
    return render(request,'update_emp.html',context=context)

def update_single(request,pk):
    employee=Employee.objects.get(id=pk)
    form=updaterecordform(instance=employee)
    if request.method=='POST':
        form=updaterecordform(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view-emp')
    
    context={'form':form}
    return render(request,'update.html',context=context)
def del_emp(request):
     employee=Employee.objects.all()
     context={'employees':employee}
     return render(request,'delete.html',context=context)
def del_single(request,pk):
     employee=Employee.objects.get(id=pk)
     employee.delete()
     return redirect('view-emp')