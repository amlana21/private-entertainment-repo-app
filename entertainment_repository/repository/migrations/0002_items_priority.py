# Generated by Django 2.2 on 2019-11-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='priority',
            field=models.CharField(choices=[('Hi', 'High'), ('Med', 'Medium'), ('Lo', 'Low')], default='Lo', max_length=64),
            preserve_default=False,
        ),
    ]
