# Generated by Django 2.2.2 on 2019-06-16 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_published'),
        ),
    ]
