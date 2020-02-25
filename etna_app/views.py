from django.shortcuts import render

from .models import *
# Create your views here.
def home(request):
    images=Ana_sehife_Sekil.objects.all()
    return render(request,'index.html',{"images":images})


def services(request):
    img=Xidmetler_Sekil.objects.first()
    return render(request, 'services.html',{"img":img})

def about(request):
    hb=Haqqimizda_basliq.objects.first()
    img=Haqqimizda_Sekil.objects.first()
    data=Haqqimizda_melumatlari.objects.all()
    return render(request, 'about.html',{"img":img,"data":data,"hb":hb,})

def contact(request):
    img=Elaqe_Sekil.objects.first()
    data=Elaqe_melumatlari.objects.first()
    return render(request, 'contact.html',{"img":img,"data":data})