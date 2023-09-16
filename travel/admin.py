from django.contrib import admin
from .models import TravelItem

@admin.register(TravelItem)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'tour_date')
    list_filter = ('tour_date',)
    search_fields = ('name', 'description')

# list_displayопределяет поля, которые будут отображаться в виде списка панели администратора.
# list_filterпозволяет фильтровать направления по дате тура.
# search_fieldsпозволяет осуществлять поиск по имени и описанию.