from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm


def customer_form(request):
    form = CustomerForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect("customers-list")
    ctx = {
        "form":form
    }
    return render(request, "form.html",ctx)


def customers_list(request):
    customers = Customer.objects.all()
    ctx = {
        "customers": customers
    }
    return render(request,"table.html",ctx)
# Create your views here.
