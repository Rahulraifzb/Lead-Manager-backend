from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","message","owner")