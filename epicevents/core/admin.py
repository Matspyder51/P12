from django.contrib import admin
from core.models import User, Client, Contract, Event
from django import forms

# Register your models here.

admin.site.register([Client, Contract, Event])

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email", "groups")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ("id", "username", "first_name", "last_name", "email")