# Generated by Django 4.0.5 on 2022-06-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_email', models.EmailField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
