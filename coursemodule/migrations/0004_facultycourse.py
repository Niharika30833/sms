# Generated by Django 5.0 on 2024-03-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursemodule', '0003_alter_faculty_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facultyid', models.BigIntegerField(unique=True)),
                ('coursecode', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'faccou_table',
            },
        ),
    ]