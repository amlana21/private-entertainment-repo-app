# Generated by Django 2.2 on 2019-11-19 06:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTypes',
            fields=[
                ('typename', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ListTypes',
            fields=[
                ('listname', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('sourcename', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=255)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('resellprice', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('listadded', models.ManyToManyField(related_name='lists', to='repository.ListTypes')),
                ('source', models.ManyToManyField(related_name='sourcetype', to='repository.SourceType')),
                ('typeofoitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.ItemTypes')),
            ],
        ),
    ]
