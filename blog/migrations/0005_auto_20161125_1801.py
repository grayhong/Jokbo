# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161124_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2016)),
                ('semester', models.CharField(max_length=10)),
                ('quiz_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=30)),
                ('subject_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='problem_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='board',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='blog.Subject'),
        ),
        migrations.AddField(
            model_name='post',
            name='board',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Board'),
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Subject'),
        ),
    ]
