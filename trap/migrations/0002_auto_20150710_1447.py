# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='req_records',
            old_name='qwery_parameters',
            new_name='query_parameters',
        ),
    ]
