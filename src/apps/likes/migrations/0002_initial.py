# Generated by Django 4.0.5 on 2022-07-22 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(help_text='Пост, к которому относится лайк.',
                                    on_delete=django.db.models.deletion.CASCADE, to='post.post',
                                    verbose_name='liked post'),
        ),
    ]
