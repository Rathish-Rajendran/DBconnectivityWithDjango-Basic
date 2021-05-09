from django.shortcuts import render, redirect
from django.contrib import messages
from parlour_management.models import Customer,Services,Transaction,Bills,Employee

# Create your views here.
def new_customer(request) :
    if request.method == 'POST' :
        name = request.POST['customer_name']
        address = request.POST['address']
        num = request.POST['contact_num']
        age = request.POST['age']
        treat = request.POST['treatment']
        quant = request.POST['quantity']
        price = request.POST['price']
        bill = request.POST['bill_amount']

        cus_info = Customer()
        cus_info.cus_name = name
        cus_info.address = address
        cus_info.contact_num = num
        cus_info.age = age

        cus_serv = Services()
        cus_serv.treatment = treat
        cus_serv.quantity = quant

        cus_trans = Transaction()
        cus_trans.cus_name = name
        cus_trans.bill_amount = bill

        cus_bills = Bills()
        cus_bills.bill_amount = bill
        cus_bills.quantity = quant
        cus_bills.price = price

        cus_info.save()
        cus_serv.save()
        cus_trans.save()
        cus_bills.save()

        return redirect('/')
    
    else :
        return render(request, 'new_cus.html')

def old_customer(request) :
    if request.method == 'POST' :
        name = request.POST['customer_name']
        treat = request.POST['treatment']
        quant = request.POST['quantity']
        price = request.POST['price']
        bill = request.POST['bill_amount']

        cus_serv = Services()
        cus_serv.treatment = treat
        cus_serv.quantity = quant

        cus_trans = Transaction()
        cus_trans.cus_name = name
        cus_trans.bill_amount = bill

        cus_bills = Bills()
        cus_bills.bill_amount = bill
        cus_bills.quantity = quant
        cus_bills.price = price

        cus_serv.save()
        cus_trans.save()
        cus_bills.save()

        return redirect('/')
    
    else :
        return render(request, 'old_cus.html')


def employees_up(request):
    if request.method == 'POST' :
        id = request.POST["employee_id"]
        name = request.POST["employee_name"]
        num = request.POST["employee_num"]
        address = request.POST["address"]
        sal = request.POST["salary"]
        job = request.POST["job_title"]

        emp = Employee()
        emp.employee_id = id
        emp.employee_name = name
        emp.employee_num = num
        emp.address = address
        emp.salary = sal
        emp.job_title = job

        emp.save()

        return redirect('/')
    else :
        return render(request,'employees.html')

def employees_det(request) :

    if request.method == "POST" :
        num = request.POST["employee_num"]
        all_emp_det = Employee.objects.filter(employee_id = num)
        print(all_emp_det)
        return render(request,'employee_detail.html',{'emp' : all_emp_det})
    else :
        return render(request,'employee_detail.html')

def customer_det(request):
    if request.method == "POST" :
        num = request.POST["customer_num"]
        all_cus_det = Customer.objects.filter(contact_num = num)
        return render(request,'customer_details.html',{'cus' : all_cus_det})
    else :
        return render(request,'customer_details.html')
