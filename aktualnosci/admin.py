from django.contrib import admin
from .models import News, Zapytanie
from .models import Wniosek

admin.site.register(News)
admin.site.register(Wniosek)
admin.site.register(Zapytanie)