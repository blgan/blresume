# Generated by Django 4.0.3 on 2022-05-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='about',
            name='last_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]