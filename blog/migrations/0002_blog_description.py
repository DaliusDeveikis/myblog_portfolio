# Generated by Django 3.1.4 on 2020-12-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]