from django.shortcuts import render, HttpResponse
from voluntary.models import Horarios
# Create your views here.

def home(request):

    listado_vol = Horarios.objects.all()

    return render(request, "voluntary/home.html", {'voluntarys':listado_vol})
