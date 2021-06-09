from django import forms
from django.forms import ModelForm, widgets
from aktualnosci.models import Wniosek
from aktualnosci.models import Zapytanie
class WniosekForm(ModelForm):
    class Meta:
        model = Wniosek
        fields = "__all__"

        labels = {
            'nazwa': 'Name',
            'nip': 'NIP',
            'regon': 'REGON',
            'krs': 'KRS',
            'adres': 'Address',
            'branza': 'Industry',
            'forma_prawna': 'Legal form',
            'normy': 'Standard(s)',
            'zakres_dzialalnosci': 'Scope of activity',
            'liczba_zatrudnionych': 'Total number of employees',
            'liczba_zatrudnionych_system': 'Employes covered by the system',
            'miejsce': 'Place',
            'przedstawiciel': 'Representative',
            'zrodlo': 'How did you find Polcargo?',
        }

        widgets = {
            'nazwa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company name'}),
            'nip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'NIP number'}),
            'regon': forms.TextInput(attrs={'class':'form-control', 'placeholder':'REGON number'}),
            'krs': forms.TextInput(attrs={'class':'form-control', 'placeholder':'KRS number'}),
            'adres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company address'}),
            'branza': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sector of activity'}),
            'forma_prawna': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Legal form of business activity'}),
            'normy': forms.TextInput(attrs={'class':'form-control', 'placeholder':'The standard(s) to which you intend to certify your organization'}),
            'zakres_dzialalnosci': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Scope of activity subject to certification'}),
            'liczba_zatrudnionych': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total number of employees'}),
            'liczba_zatrudnionych_system': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number of employees in the area covered by the system'}),
            'miejsce': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Place of operation'}),
            'przedstawiciel': forms.TextInput(attrs={'class':'form-control', 'placeholder':'(name, position, contact)'}),
            'zrodlo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'From what source did you learn about Polcargo Group\'s certification activities?'}),

        }

class ZapytanieForm(ModelForm):
    class Meta:
        model = Zapytanie
        fields = "__all__"
        labels = {
            'nazwa': 'Name',
            'adres': 'Address',
            'tel': 'Telephone',
            'fax': 'Fax',
            'internet': 'Internet',
            'nip': 'NIP',
            'krs': 'KRS',
            'prezes': 'President/Director',
            'email': 'E-mail',
            'przedmiot_dzialalnosci': 'Subject of activity',
            'imie': 'Name',
            'nazwisko': 'Surname',
            'stanowisko': 'Position',
            'telefon': 'Telephone',
            'email2': 'E-mail',
            'norma': 'Standard',
            'certyfikat': 'Certificate',
            'liczba_zatrudnionych': 'Total number of employees',
            'liczba_zatrudnionych_system': 'Employees in the area covered by the system',
            'zakres': 'Scope of activity',
        }
        widgets = {
            'nazwa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full company name'}),
            'adres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address of the organization'}),
            'tel': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telephone'}),
            'fax': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fax'}),
            'internet': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Internet of company'}),
            'nip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'NIP number'}),
            'krs': forms.TextInput(attrs={'class':'form-control', 'placeholder':'KRS number'}),
            'prezes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company President/Director'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company e-mail address'}),
            'przedmiot_dzialalnosci': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject of the company\'s activity'}),
            'imie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of contact person'}),
            'nazwisko': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname of contact person'}),
            'stanowisko': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Position of contact person'}),
            'telefon': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number of contact person'}),
            'email2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail address of contact person'}),
            'norma': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please enter the standard(s) to which you intend to certify your management system.'}),
            'certyfikat': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Is or has the company certified or implemented a management system? YES/NO. If YES, what kind and by whom issued/implemented:'}),
            'liczba_zatrudnionych': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total number of employees'}),
            'liczba_zatrudnionych_system': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number of employees in the area covered by the system'}),
            'zakres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Scope of activity subject to certification'}),
        }
