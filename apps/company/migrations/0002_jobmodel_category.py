# Generated by Django 4.2.5 on 2023-09-29 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
