# Generated by Django 5.0.4 on 2024-06-03 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_agentrating_average_rating'),
        ('blog', '0004_alter_post_author_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.agent'),
        ),
    ]