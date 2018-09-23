from django.contrib import admin
from .models import Voluntary
from .models import Horarios
# Register your models here.

@admin.register(Voluntary)

class VoluntaryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name','surname','address','email','tlf')
    search_fields = (

        'name',
        'surname',
        'tlf',
        'address',
    )


@admin.register(Horarios)
class HorariosAdmin(admin.ModelAdmin):
   
   readonly_fields = ('fromto','to')
   
   list_filter = (

        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    )



 