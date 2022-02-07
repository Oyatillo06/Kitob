from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import KitobForm,MuallifForm
from .models import *
def homepage(request):
    return render(request, "home.html")
def name(request):
    return HttpResponse("Men,Sharobiddinov Oyatillo 16-oktyabr 2006-yilda Margilonda tugilganman")
def kitoblar(request):
    if request.method=='POST':
        forma=KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect("kitoblar")

    kitob=Kitob.objects.all()
    forma=KitobForm()
    return render(request,'kitoblar.html',{'books':kitob,'forma':forma})

def record(request):
    if request.method=='POST':
        Record.objects.create(
            muallif=request.POST.get("muallif"),
            kitob=request.POST["kitob"],
            olingan_sana=request.POST["olingan_sana"]

        )
        return redirect("record")



    rec=Record.objects.all()
    return render(request,"record.html",{"b":rec})
def record_ochir(request,son):
    r=Record.objects.get(id=son)
    r.delete()
    return redirect("record")
def mualliflar(request):
    if request.method=='POST':
        forma=MuallifForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect("mualliflar")
    muallif = Muallif.objects.all()
    forma=MuallifForm()
    return render(request, "mualliflar.html", {"muallif": muallif,"forma":forma})

def muallif_ochir(request,son):
    m=Muallif.objects.get(id=son)
    m.delete()
    return redirect("mualliflar")
def kitob_ochir(request,son):
    k=Kitob.objects.get(id=son)
    k.delete()
    return redirect("kitoblar")


