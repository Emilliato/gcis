# Generated by Django 2.2.2 on 2019-06-15 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=25)),
                ('date_created', models.DateTimeField(verbose_name='date_published')),
            ],
        ),
        migrations.CreateModel(
            name='IProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('p_code', models.CharField(max_length=10)),
                ('p_quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=25)),
                ('p_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=25)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Invoice')),
            ],
        ),
    ]
