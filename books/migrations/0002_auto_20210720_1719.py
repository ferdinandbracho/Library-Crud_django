# Generated by Django 3.2.5 on 2021-07-20 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuthorModel',
            new_name='Author',
        ),
        migrations.RenameModel(
            old_name='BookModel',
            new_name='Book',
        ),
    ]