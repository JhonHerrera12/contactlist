
from django.urls import path

from contacts import views


urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),

]
