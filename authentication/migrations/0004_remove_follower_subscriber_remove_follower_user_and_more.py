# Generated by Django 4.0.3 on 2022-05-09 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_profile_picture_profile_photosrc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='subscriber',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]