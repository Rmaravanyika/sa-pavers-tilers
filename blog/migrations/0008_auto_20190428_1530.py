# Generated by Django 2.0 on 2019-04-28 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190428_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freequote',
            old_name='service_req',
            new_name='service_required',
        ),
    ]
