from django.shortcuts import render, HttpResponse
from datetime import date
from .models import AddOrder, Promotion, PromotionUsage
from .serializers import PromotionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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

        if quantity < 0 or quantity > 25:
            return HttpResponse('Error, Quantity is invalid. Please pick a valid number')
        if delivery_date < str(date.today()):
            return HttpResponse('Error, Date is invalid. Please pick a valid date')
        if delivery_time==None:
            return HttpResponse('Please select a delivery time')

        new_order = AddOrder(quantity=quantity, delivery_date=delivery_date, name=name,
                             email=email, phone=phone, comments=comments, delivery_time=delivery_time)
        new_order.save()
    return render(request, "order.html")

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
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
