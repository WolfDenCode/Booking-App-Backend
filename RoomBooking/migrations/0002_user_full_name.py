# Generated by Django 5.1.3 on 2024-11-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomBooking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]