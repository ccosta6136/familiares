from django.shortcuts import render
from django.http import HttpResponse
from familiares_app.models import Familiares

# Create your views here.
def listar_familiares(request):
    context = {}
    context["familiares"] = Familiares.objects.all()
    return render(request, "familiares_app/index.html", context)