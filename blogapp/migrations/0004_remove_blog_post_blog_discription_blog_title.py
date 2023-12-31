# Generated by Django 4.2.2 on 2023-06-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_blogger_nationality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='post',
        ),
        migrations.AddField(
            model_name='blog',
            name='discription',
            field=models.TextField(default=1, help_text='Title of the blog (e.g Success of Hardworker)', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.TextField(default=1, help_text='Title of the blog (e.g Success of Hardworker)', max_length=50, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
