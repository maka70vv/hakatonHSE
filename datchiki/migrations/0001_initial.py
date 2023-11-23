# Generated by Django 4.2.7 on 2023-11-23 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arduino', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Okno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opened', models.BooleanField(default=False)),
                ('idWindow', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='okoshko', to='arduino.windows')),
            ],
        ),
    ]
