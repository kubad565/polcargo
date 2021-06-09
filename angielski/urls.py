from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('quality/', views.quality, name='quality'),
    path('shareholders/', views.shareholders, name='shareholders'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('offer/', views.offer, name='offer'),
    path('rules/', views.rules, name='rules'),
    path('ask/', views.ask, name='ask'),
    path('request/', views.request, name='request'),
    path('faq/', views.faq, name='faq'),
    path('description/', views.description, name='description'),
    path('news/<int:pk>/', views.news_detail, name='news_detail2'),
]

