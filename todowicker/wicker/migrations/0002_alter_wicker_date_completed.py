# Generated by Django 3.2.5 on 2021-07-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wicker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wicker',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
