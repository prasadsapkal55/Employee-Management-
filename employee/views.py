from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from employee.forms import EmployeeForm
from employee.models import Employee

def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Employee added successfully!')
                return redirect('/show/')
            except Exception as e:
                messages.error(request, f'Error adding employee: {str(e)}')
    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})
    
def show(request):
    employees=Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def edit(request,id):
    employee = get_object_or_404(Employee, id=id)
    return render(request,'edit.html',{'employee':employee}) 

def update(request,id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully!')
            return redirect("/show/")
        else:
            messages.error(request, 'Please correct the errors below.')
    return render(request,'edit.html',{'employee':employee})

def destroy(request,id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully!')
    return redirect("/show/")



