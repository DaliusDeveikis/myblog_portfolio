# Generated by Django 3.1.4 on 2020-12-14 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='discription',
            new_name='description',
        ),
    ]