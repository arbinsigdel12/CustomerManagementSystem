from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    orders=Order.objects.all()
    employees=Employee.objects.all()
    total_orders=orders.count()
    total_completed=orders.filter(status='Completed').count()
    total_incompleted=orders.filter(status='Incompleted').count()
    context={'orders':orders,'employees':employees,'total_orders':total_orders,'total_completed':total_completed,'total_incompleted':total_incompleted}
    return render(request,'accounts/dashboard.html',context)
def employee(request,pk):
    employee=Employee.objects.get(id=pk)
    orders=employee.order_set.all()
    order_count=orders.count()
    context={'employee':employee,'orders':orders,'order_count':order_count}
    return render(request,'accounts/employee.html',context)
def works(request):
    works=Work.objects.all()
    return render(request,'accounts/works.html',{'works':works})