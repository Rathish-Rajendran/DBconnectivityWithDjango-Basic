from django.urls import path
from . import views
urlpatterns = [
    path('new_customer',views.new_customer, name = 'new_customer'),
    path('old_customer',views.old_customer, name = 'old_customer'),
    path('employees_up', views.employees_up, name = 'employees_up'),
    path('employees_det',views.employees_det,name = 'employees_det'),
    path('customer_det',views.customer_det, name = 'customer_det')
]