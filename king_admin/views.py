# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import importlib

import king_admin

# Create your views here.

def index(request):
    return render(request, "king_admin/table_index.html", {
        'table_list': king_admin.enabled_admins
    })

def display_table_objs(request, app_name, table_name):

    # model_module = importlib.import_module('%s.models' % app_name)
    # model_obj = getattr(model_module, table_name)
    admin_class = king_admin.enabled_admins[app_name][table_name]

    return render(request, "king_admin/table_objs.html", {
        "admin_class": admin_class
    })
