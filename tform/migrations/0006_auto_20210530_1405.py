# Generated by Django 3.2.3 on 2021-05-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tform', '0005_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tform',
            name='client_code',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tform',
            name='mobile_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]