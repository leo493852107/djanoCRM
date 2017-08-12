#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Leo'
__date__ = '2017/8/8'


from crm import models

enabled_admins = {}


class BaseAdmin(object):
    list_display = []
    list_filter = []


class CustomerAdmin(BaseAdmin):
    list_display = ['qq', 'name', 'source', 'consultant', 'consult_course', 'date', 'memo']


class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ['customer', 'consultant', 'date']


def register(model_class, admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label] = {}

    # 绑定model 对象和admin类
    admin_class.model = model_class
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class


register(models.Customer, CustomerAdmin)
register(models.CustomerFollowUp, CustomerFollowUpAdmin)