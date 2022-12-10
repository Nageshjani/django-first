from django.shortcuts import render,redirect
from employee.form import EmployeeForm
from employee.models import Employee

def show(request):
    data=Employee.objects.all()
    return render(request,'show.html',{'data':data})

def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form =EmployeeForm()
    return render(request,'emp.html',{'form':form})

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'form':employee})

def update(request,id):
    employee=Employee.objects.get(pk=id)
    form= EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')

def destroy(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')





