# Generated by Django 2.2.3 on 2019-07-27 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sudo',
            old_name='FaName',
            new_name='Fa_Name',
        ),
    ]