# Generated by Django 4.1.1 on 2022-11-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_event_flier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='flier',
            field=models.ImageField(default='flyer.png', null=True, upload_to=''),
        ),
    ]
