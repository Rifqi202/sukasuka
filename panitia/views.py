from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from . import models

# Create your views here.

def dash(request):
    if request.method == 'POST':
        models.judul.objects.create(
            judul = request.POST['judul']
            )
        return redirect ('dash')
    judul = models.judul.objects.all()
    return render(request, 'dash.html',{
        'judul': judul,
    })

def dashboard(request):
    return render(request, 'dashboard.html')

def daftarkandidat(request):
    return render(request, 'daftarkandidat.html')

def datapemilih(request):
    return render(request, 'datapemilih.html')

def datavoting(request):
    return render(request, 'datavoting.html')

def tambahpanitia(request):
    return render(request, 'tambahpanitia.html')

