# Generated by Django 3.2.8 on 2021-10-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indobyte_employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_id', models.CharField(max_length=20)),
                ('emp_address', models.TextField()),
                ('emp_salary', models.IntegerField()),
            ],
        ),
    ]
