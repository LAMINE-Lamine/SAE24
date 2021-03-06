# Generated by Django 4.0.4 on 2022-06-22 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='capteur',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('piece', models.CharField(max_length=100)),
                ('emplacement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=200)),
                ('timestamp', models.CharField(max_length=200)),
                ('capteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mySAE24.capteur')),
            ],
        ),
    ]
