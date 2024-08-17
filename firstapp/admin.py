from django.contrib import admin
from .models import Customer


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "job", "country", "phone", "email")
    search_fields = ("name", "company", "email")
