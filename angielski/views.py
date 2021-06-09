from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage
from aktualnosci.models import News
from .forms import WniosekForm
from django.http import HttpResponseRedirect
from aktualnosci.models import Zapytanie
from .forms import ZapytanieForm

def news_list(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(news, 5) #zmiana ilosci wyswietlanych newsow
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = paginator.page(1)

    return render(request=request, template_name='angielski/news_list.html', context={'news' : page_obj})
    #return render(request, 'angielski/news_list.html', {})

def request(request):
    submitted = False
    if request.method == "POST":
        form = WniosekForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/en/request?submitted=True')
    else:
        form = WniosekForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'angielski/request.html', {'form': form, 'submitted':submitted})

def offer(request):
    submitted = False
    if request.method == "POST":
        form = ZapytanieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/en/offer?submitted=True')
    else:
        form = ZapytanieForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'angielski/offer.html', {'form': form, 'submitted':submitted})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'angielski/news_detail.html', {'news': news})

def about(request):
    return render(request, 'angielski/about.html', {})

def shareholders(request):
    return render(request, 'angielski/shareholders.html', {})

def contact(request):
    return render(request, 'angielski/contact.html', {})

def quality(request):
    return render(request, 'angielski/quality.html', {})

def rules(request):
    return render(request, 'angielski/rules.html', {})


def ask(request):
    return render(request, 'angielski/ask.html', {})

def catalog(request):
    return render(request, 'angielski/catalog.html', {})
    
def faq(request):
    return render(request, 'angielski/faq.html', {})

def description(request):
    return render(request, 'angielski/description.html', {})


