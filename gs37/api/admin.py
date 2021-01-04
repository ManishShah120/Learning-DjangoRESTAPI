from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']
