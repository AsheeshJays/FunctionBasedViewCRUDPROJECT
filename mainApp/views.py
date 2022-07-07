from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Employee
from .forms import EmployeeRegistration

def AddShow(request):
    if request.method == "POST":
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            empID = fm.cleaned_data['empID']
            empName = fm.cleaned_data['empName']
            empDesgination = fm.cleaned_data['empDesgination']
            empSalary = fm.cleaned_data['empSalary']
            reg = Employee(empID=empID,empName=empName,empDesgination=empDesgination,empSalary=empSalary)
            reg.save()
            fm = EmployeeRegistration()
    else:
        fm = EmployeeRegistration()
    emp = Employee.objects.all()
    return render(request, 'add&show.html',{'form':fm,'employee':emp})

def delete(request, id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return HttpResponseRedirect('/')

def edit(request, id):
    emp = Employee.objects.get(pk=id)
    fm = EmployeeRegistration(request.POST, instance=emp)
    if fm.is_valid():
        fm.save()
    else:
        emp = Employee.objects.get(pk=id)
        fm = EmployeeRegistration(instance=emp)
    return render(request, 'update.html',{'form':fm})