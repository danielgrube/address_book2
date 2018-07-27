# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    phone_number = models.IntegerField(default = 0)
    email = models.EmailField()
    street_address = models.CharField(max_length = 300)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

    def get_absolute_url(self):
        return reverse('contacts:contact_edit', kwargs={'pk': self.pk})