# Generated by Django 3.2.3 on 2021-05-19 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_email', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=30)),
                ('job_description', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField()),
            ],
        ),
    ]
