# Generated by Django 4.2.7 on 2023-11-23 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arduino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='windows',
            name='idDevice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='windows', to='arduino.arduinodevices'),
        ),
    ]