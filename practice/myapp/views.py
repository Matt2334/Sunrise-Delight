from django.shortcuts import render, HttpResponse
from datetime import date
# Create your views here.
def home(request):
    return render(request, "home.html")
def order(request):
    if request.method == "POST":
        topping = request.POST["Topping(s)"]
        quantity = int(request.POST["Quantity"])
        delivery_date = request.POST["Delivery Date"]
        name = request.POST["Name"]
        email = request.POST["Email"]
        phone = request.POST["Phone"]
        comments = request.POST["Additional Comments"]
        delivery_time = request.POST.get("Delivery Times")

        if quantity < 0 or quantity > 25:
            return HttpResponse('Error, Quantity is invalid. Please pick a valid number')
        if delivery_date < str(date.today()):
            return HttpResponse('Error, Date is invalid. Please pick a valid date')
        if delivery_time==None:
            return HttpResponse('Please select a delivery time')
        print(name, email, phone, topping, quantity, delivery_date, delivery_time, comments)
    return render(request, "order.html")