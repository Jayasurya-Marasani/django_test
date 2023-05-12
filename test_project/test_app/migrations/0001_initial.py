# Generated by Django 4.1.7 on 2023-04-28 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=1)),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.program')),
            ],
        ),
    ]
