from django.contrib import admin
from .models import Orderer, Order, Store, Baker, Review, DetailedOption, Cake, checkBaker, checkOrderer

# Register your models here.

admin.site.register(checkOrderer)
admin.site.register(Orderer)
admin.site.register(checkBaker)
admin.site.register(Baker)
admin.site.register(Store)
admin.site.register(Cake)
admin.site.register(DetailedOption)
admin.site.register(Order)
admin.site.register(Review)