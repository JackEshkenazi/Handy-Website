from django.contrib import admin
from .models import Contractor, City

class ContractorCity(admin.TabularInline):
    model = City
    extra = 1

# Register your models here.
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    ordering = ('name',)
    search_fields = ('name', 'phone')
    inline = (ContractorCity,)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

