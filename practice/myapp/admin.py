from django.contrib import admin
from myapp.models import AddOrder, Promotion, PromotionUsage

# Register your models here.
admin.site.register(AddOrder)
admin.site.register(Promotion)
admin.site.register(PromotionUsage)
