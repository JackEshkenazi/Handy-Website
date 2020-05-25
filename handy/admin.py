from django.contrib import admin
from .models import Contractor, City

# Register your models here.
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    ordering = ('name',)
    search_fields = ('name', 'phone')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

