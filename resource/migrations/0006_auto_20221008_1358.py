# Generated by Django 3.2.15 on 2022-10-08 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0005_delete_site1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IDC',
            new_name='Site',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='DC_id',
            new_name='site_id',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='DC_name',
            new_name='site_name',
        ),
    ]
