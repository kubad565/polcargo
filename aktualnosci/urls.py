from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('onas/', views.onas, name='onas'),
    path('jakosc/', views.jakosc, name='jakosc'),
    path('udzial/', views.udzial, name='udzial'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('zasady/', views.zasady, name='zasady'),
    path('oferta/', views.oferta, name='oferta'),
    path('wniosek/', views.wniosek, name='wniosek'),
    path('katalog/', views.katalog, name='katalog'),
    path('zapytanie/', views.zapytanie, name='zapytanie'),
    path('faq/', views.faq, name='faq'),

]
