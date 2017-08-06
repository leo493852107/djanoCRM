# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from crm import views

urlpatterns = [
    url(r'^$', views.index, name="sales_index"),
    url(r'^customers/$', views.customer_list, name="customer_list"),
]
