from django.contrib import admin
from core.models import User, Client, Contract, Event

# Register your models here.

admin.site.register([User, Client, Contract, Event])