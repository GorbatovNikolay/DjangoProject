# Generated by Django 4.0.5 on 2022-06-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True,
                                    help_text='Upload files in .JPG or .PNG formats only! .HEIC is not supported yet.',
                                    upload_to='user/avatars/'),
        ),
    ]