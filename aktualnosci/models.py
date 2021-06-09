from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to="images/")
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    text = models.TextField()

    eng_title = models.CharField(max_length=50)
    eng_subtitle = models.CharField(max_length=200,)
    eng_text = models.TextField()

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Wniosek(models.Model):
    nazwa =  models.CharField(max_length=50)
    nip = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    regon = models.CharField(max_length=14, validators=[RegexValidator(r'^\d{1,10}$')])
    krs = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
    adres = models.CharField(max_length=50)
    branza = models.CharField(max_length=30)
    forma_prawna = models.CharField(max_length=50)
    normy = models.CharField(max_length=100)
    zakres_dzialalnosci = models.CharField(max_length=100)
    liczba_zatrudnionych = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')])
    liczba_zatrudnionych_system = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')])
    miejsce = models.CharField(max_length=50)
    przedstawiciel = models.CharField(max_length=200)
    zrodlo = models.CharField(max_length=30, blank=True)
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.nazwa

class Zapytanie(models.Model):
    nazwa = models.CharField(max_length=50)
    adres = models.CharField(max_length=50)
    tel = models.CharField(max_length=11, blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
    nip = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    internet = models.CharField(max_length=30)
    prezes = models.CharField(max_length=30)
    krs = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
    przedmiot_dzialalnosci = models.CharField(max_length=30)
    fax = models.CharField(max_length=40, validators=[RegexValidator(r'^\d{1,10}$')])
    email = models.CharField(max_length=50)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    stanowisko = models.CharField(max_length=50)
    telefon = models.CharField(max_length=11, blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
    email2 = models.CharField(max_length=50)
    norma = models.CharField(max_length=50)
    certyfikat = models.CharField(max_length=50)
    liczba_zatrudnionych = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')])
    liczba_zatrudnionych_system = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')])
    zakres = models.CharField(max_length=200)
    
    def publish(self):
        self.save()
        
    def __str__(self):
        return self.nazwa