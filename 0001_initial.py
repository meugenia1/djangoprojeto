# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=40)),
                ('preco', models.IntegerField()),
                ('descricao', models.CharField(max_length=140)),
                ('destaque', models.BooleanField(default=False, verbose_name='Destaque')),
                ('data', models.CharField(blank=True, max_length=30)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coded.Categoria')),
            ],
        ),
    ]
