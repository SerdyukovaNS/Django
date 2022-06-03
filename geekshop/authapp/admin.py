from django.contrib import admin

# Register your models here.
from authapp.models import User
from basket.models import Basket
from basket.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = Basket
    inlines = (BasketAdmin,)