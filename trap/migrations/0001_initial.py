# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='req_records',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('req_date', models.DateTimeField(verbose_name=b'Date of request')),
                ('rem_ip', models.GenericIPAddressField(verbose_name=b'Field for IP adresses')),
                ('req_method', models.CharField(max_length=20)),
                ('scheme', models.CharField(max_length=10)),
                ('query_string', models.TextField()),
                ('qwery_parameters', models.TextField()),
                ('cookies', models.TextField()),
                ('headers', models.TextField()),
            ],
        ),
    ]
