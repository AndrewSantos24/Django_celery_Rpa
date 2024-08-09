from django.contrib import admin
from stocks.models import stock
# Register your models here.

@admin.register(stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name','price','moment',)
    search_fields =('name',)
    list_filter = ('name',)


