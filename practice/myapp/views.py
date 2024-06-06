from django.shortcuts import render, HttpResponse
from datetime import date
from .models import AddOrder, Promotion, PromotionUsage
from .serializers import PromotionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

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
        error = {}

        if quantity < 0:
            error['quantity'] = 'Quantity needs to be at-least 1'
        elif quantity > 25:
            error['quantity'] = 'Quantity can be at-most 24'
        if delivery_date <= str(date.today()):
            error['delivery_date'] =  'Please Select a valid date'
        if not name:
            error['name'] =  'Please enter your name'
        if not phone:
            error['phone'] =  'Please enter your phone number'
        if error:
            return render(request, "order.html", {
                'quantity': quantity,
                'delivery_date': delivery_date,
                'name': name,
                'email': email,
                'phone': phone,
                'comments': comments,
                'delivery_time': delivery_time,
                'error': error,
            })
        new_order = AddOrder(quantity=quantity, delivery_date=delivery_date, name=name, email=email, phone=phone,
                             comments=comments, delivery_time=delivery_time)
        new_order.save()
        # return render("/success")
    return render(request, "order.html")



class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def apply_promotion(self, request):
        code = request.data.get("code")
        user = request.user

        try:
            promotion = Promotion.objects.get(code=code)
            if PromotionUsage.objects.filter(promotion=promotion, user=user).exists():
                return Response({'success': False, 'message': 'You have already used this promotion.'})
            PromotionUsage.objects.create(promotion=promotion, user=user)
            return Response({'success':True, 'discount_value':promotion.discount_value, 'discount_type':promotion.discount_type})
        except Promotion.DoesNotExist:
            return Response({'success':False, 'message':'Promotion Code does not exist.'})

