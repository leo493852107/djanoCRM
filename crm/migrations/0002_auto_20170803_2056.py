# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': '\u6821\u533a', 'verbose_name_plural': '\u6821\u533a'},
        ),
        migrations.AlterModelOptions(
            name='classlist',
            options={'verbose_name': '\u73ed\u7ea7', 'verbose_name_plural': '\u73ed\u7ea7'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '\u8bfe\u7a0b\u8868', 'verbose_name_plural': '\u8bfe\u7a0b\u8868'},
        ),
        migrations.AlterModelOptions(
            name='courserecord',
            options={'verbose_name': '\u4e0a\u8bfe\u8bb0\u5f55', 'verbose_name_plural': '\u4e0a\u8bfe\u8bb0\u5f55'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': '\u5ba2\u6237\u8868', 'verbose_name_plural': '\u5ba2\u6237\u8868'},
        ),
        migrations.AlterModelOptions(
            name='customerfollowup',
            options={'verbose_name': '\u5ba2\u6237\u8ddf\u8fdb\u8bb0\u5f55', 'verbose_name_plural': '\u5ba2\u6237\u8ddf\u8fdb\u8bb0\u5f55'},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name_plural': '\u62a5\u540d\u8868'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name_plural': '\u7f34\u8d39\u8bb0\u5f55'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name_plural': '\u89d2\u8272'},
        ),
        migrations.AlterModelOptions(
            name='studyrecord',
            options={'verbose_name': '\u5b66\u4e60\u8bb0\u5f55', 'verbose_name_plural': '\u5b66\u4e60\u8bb0\u5f55'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': '\u8d26\u53f7\u8868'},
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('students', 'course_record')]),
        ),
    ]
