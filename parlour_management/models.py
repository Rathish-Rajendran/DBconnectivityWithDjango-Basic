from django.db import models

# Create your models here.
class Customer(models.Model) :
    cus_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    contact_num = models.BigIntegerField()
    age = models.IntegerField()

class Services(models.Model) :
    treatment = models.CharField(max_length = 100)
    quantity = models.CharField(max_length = 100)

class Transaction(models.Model) :
    cus_name = models.CharField(max_length = 100)
    bill_amount = models.IntegerField()

class Bills(models.Model) :
    bill_amount = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField() 

class Employee(models.Model) :
    employee_id = models.BigIntegerField()
    employee_name = models.CharField(max_length = 100)
    employee_num = models.BigIntegerField()
    address = models.CharField(max_length = 100)
    salary = models.IntegerField()
    job_title = models.CharField(max_length = 100)






