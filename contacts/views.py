# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from contacts.models import Contact

class ContactsForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'street_address']

def contact_list(request, template_name='contacts/contacts_list.html'):
    contact = Contact.objects.all()
    data = {}
    data['contact_list'] = contact
    return render(request, template_name, data)

def contact_view(request, pk, template_name='contacts/contacts_detail.html'):
    contact= get_object_or_404(Contact, pk=pk)    
    return render(request, template_name, {'contact':contact})

def contact_create(request, template_name='contacts/contacts_form.html'):
    form = ContactsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contacts:contact_list')
    return render(request, template_name, {'form':form})

def contact_update(request, pk, template_name='contacts/contact_form.html'):
    contact= get_object_or_404(Contact, pk=pk)
    form = ContactsForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contacts:contact_list')
    return render(request, template_name, {'form':form})

def contact_delete(request, pk, template_name='contacts/contacts_confirm_delete.html'):
    contact= get_object_or_404(Contact, pk=pk)    
    if request.method=='POST':
        contact.delete()
        return redirect('contacts:contact_list')
    return render(request, template_name, {'contact':contact})