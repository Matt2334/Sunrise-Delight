from rest_framework import serializers
from .models import Promotion, PromotionUsage

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ["code", "discount_type", "discount_value"]
class PromotionUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionUsage
        fields = ["promotion", "user", "date_used"]
