# Generated by Django 3.1.7 on 2021-04-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210414_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenfers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passemgers', to='flights.Flight')),
            ],
        ),
    ]
