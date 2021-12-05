from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    email = models.EmailField(max_length=100)


class Client(models.Model):

    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'selling_team'})


class Event(models.Model):

    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'support_team'})
    event_status = models.BooleanField(default=False)
    attendees = models.PositiveIntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()


class Contract(models.Model):

    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'selling_team'})
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment = models.DateTimeField(null=True)
