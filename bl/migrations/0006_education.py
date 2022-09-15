# Generated by Django 4.0.3 on 2022-05-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bl', '0005_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('certificate', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('cgpa', models.FloatField()),
            ],
        ),
    ]