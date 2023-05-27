import genericpath
from django.shortcuts import render

from django.views import generic

from contacts.models import Contact

# Create your views here.
class ContactListView(generic.ListView):
    model = Contact
    