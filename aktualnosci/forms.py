from django import forms
from django.forms import ModelForm, widgets
from .models import Wniosek
from .models import Zapytanie

class WniosekForm(ModelForm):
    class Meta:
        model = Wniosek
        fields = "__all__"

        labels = {
            'nazwa': 'Nazwa',
            'nip': 'NIP',
            'regon': 'REGON',
            'krs': 'KRS',
            'adres': 'Adres',
            'branza': 'Branża',
            'forma_prawna': 'Forma prawna',
            'normy': 'Norma/normy',
            'zakres_dzialalnosci': 'Zakres działalności',
            'liczba_zatrudnionych': 'Całkowita liczba pracowników',
            'liczba_zatrudnionych_system': 'Pracownicy w obszarze objętym systemem',
            'miejsce': 'Miejsce',
            'przedstawiciel': 'Przedstawiciel',
            'zrodlo': 'Jak znalazłeś/aś Polcargo?',
        }

        widgets = {
            'nazwa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nazwa firmy'}),
            'nip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numer NIP'}),
            'regon': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numer REGON'}),
            'krs': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numer KRS'}),
            'adres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres firmy'}),
            'branza': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Branża prowadzonej działalności'}),
            'forma_prawna': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Forma prawna prowadzonej działalności'}),
            'normy': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Norma/normy na zgodność, z którą/którymi zamierzają państwo certyfikować swoją organizację'}),
            'zakres_dzialalnosci': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zakres działalności podlegający certyfikacji'}),
            'liczba_zatrudnionych': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Całkowita liczba zatrudnionych pracowników'}),
            'liczba_zatrudnionych_system': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Liczba zatrudnionych pracowników w obszarze objętym systemem'}),
            'miejsce': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Miejsce prowadzenia działalności'}),
            'przedstawiciel': forms.TextInput(attrs={'class':'form-control', 'placeholder':'(imię i nazwisko, stanowisko, kontakt)'}),
            'zrodlo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Z jakiego źródła dowiedzieliście się Państwo o działalności certyfikacyjnej Polcargo Group?'}),

        }

class ZapytanieForm(ModelForm):
    class Meta:
        model = Zapytanie
        fields = "__all__"
        labels = {
            'nazwa': 'Nazwa',
            'adres': 'Adres',
            'tel': 'Telefon',
            'fax': 'Fax',
            'internet': 'Internet',
            'nip': 'NIP',
            'krs': 'KRS',
            'prezes': 'Prezes/Dyrektor',
            'email': 'E-mail',
            'przedmiot_dzialalnosci': 'Przedmiot działalności',
            'imie': 'Imię',
            'nazwisko': 'Nazwisko',
            'stanowisko': 'Stanowisko',
            'telefon': 'Telefon',
            'email2': 'E-mail',
            'norma': 'Norma',
            'certyfikat': 'Certyfikat',
            'liczba_zatrudnionych': 'Całkowita liczba pracowników',
            'liczba_zatrudnionych_system': 'Pracownicy w obszarze objętym systemem',
            'zakres': 'Zakres działalności',
        }
        widgets = {
            'nazwa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pełna nazwa firmy'}),
            'adres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres organizacji'}),
            'tel': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefon'}),
            'fax': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fax'}),
            'internet': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Internet firmy'}),
            'nip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numer NIP'}),
            'krs': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numer KRS'}),
            'prezes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prezes/Dyrektor firmy'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres e-mail firmy'}),
            'przedmiot_dzialalnosci': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Przedmiot działalności firmy'}),
            'imie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imię osoby kontaktowej'}),
            'nazwisko': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nazwisko osoby kontaktowej'}),
            'stanowisko': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Stanowisko osoby kontaktowej'}),
            'telefon': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefon osoby kontaktowej'}),
            'email2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres e-mail osoby kontaktowej'}),
            'norma': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Proszę wpisać normę/normy na zgodność, z którą/którymi zamierzają Państwo certyfikować swój system zarządzania.'}),
            'certyfikat': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Czy firma posiada lub posiadała certyfikat lub wdrożony system zarządzania? TAK/NIE. Jeżeli TAK, to jaki i przez kogo wydany/wdrożony:'}),
            'liczba_zatrudnionych': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Całkowita liczba zatrudnionych pracowników'}),
            'liczba_zatrudnionych_system': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Liczba zatrudnionych pracowników w obszarze objętym systemem'}),
            'zakres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zakres działalności podlegający certyfikacji'}),
        }
