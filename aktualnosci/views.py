from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import News, Zapytanie
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage
from .forms import WniosekForm
from .forms import ZapytanieForm
from django.http import HttpResponseRedirect

# Create your views here.
def news_list(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(news, 5) #zmiana ilosci wyswietlanych newsow
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = paginator.page(1)

    return render(request=request, template_name='aktualnosci/news_list.html', context={'news' : page_obj})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'aktualnosci/news_detail.html', {'news': news})


def wniosek(request):
    submitted = False
    if request.method == "POST":
        form = WniosekForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/wniosek?submitted=True')
    else:
        form = WniosekForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'aktualnosci/wniosek.html', {'form': form, 'submitted':submitted})


def zapytanie(request):
    submitted = False
    if request.method == "POST":
        form = ZapytanieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapytanie?submitted=True')
    else:
        form = ZapytanieForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'aktualnosci/zapytanie.html', {'form': form, 'submitted':submitted})



def onas(request):
    return render(request, 'aktualnosci/onas.html', {})

def jakosc(request):
    return render(request, 'aktualnosci/jakosc.html', {})

def udzial(request):
    return render(request, 'aktualnosci/udzial.html', {})

def kontakt(request):
    return render(request, 'aktualnosci/kontakt.html', {})

def zasady(request):
    return render(request, 'aktualnosci/zasady.html', {})

def oferta(request):
    return render(request, 'aktualnosci/oferta.html', {})

def katalog(request):
    return render(request, 'aktualnosci/katalog.html', {})


def faq(request):
    return render(request, 'aktualnosci/faq.html', {})











