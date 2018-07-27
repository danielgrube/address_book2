from django.conf.urls import url

from contacts import views

urlpatterns = [
    url(r'^$', views.contact_list, name = 'contact_list',),
    url(r'^view/<int:pk>/$', views.contact_view, name = 'contact_view',),
    url(r'^new/$', views.contact_create, name = 'contact_new',),
    url(r'^edit/<int:pk>/$', views.contact_update, name = 'contact_edit',),
    url(r'^delete/<int:pk>/$', views.contact_delete, name = 'contact_delete',),
]