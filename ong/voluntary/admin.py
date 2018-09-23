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



class HorariosAdmin(admin.ModelAdmin):
    pass




admin.site.register(Horarios,HorariosAdmin)