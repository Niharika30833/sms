# Generated by Django 5.0 on 2024-02-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(choices=[('CSE(R)', 'CSE(Regular)'), ('CSE(H)', 'CSE(HONORS)'), ('CSE&IT', 'CSIT')], max_length=100)),
                ('program', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech')], max_length=50)),
                ('academicyear', models.CharField(choices=[('2023-24', '2023-24'), ('2022-23', '2022-23')], max_length=20)),
                ('semester', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10)),
                ('year', models.IntegerField()),
                ('coursecode', models.CharField(max_length=20)),
                ('coursetitle', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'course_table',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facultyid', models.BigIntegerField(unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=20)),
                ('department', models.CharField(choices=[('CSE(R)', 'CSE(Regular)'), ('CSE(H)', 'CSE(HONORS)'), ('CSE&IT', 'CSIT')], max_length=50)),
                ('qualification', models.CharField(choices=[('M.Tech', 'M.Tech'), ('Ph.d', 'Ph.d')], max_length=50)),
                ('designation', models.CharField(choices=[('prof.', 'Professor'), ('Assoc.prof.', 'Associate Professor'), ('Asst prof.', 'Assintant Professor')], max_length=50)),
                ('password', models.CharField(default='klu123', max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('contact', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'faculty_table',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('studentid', models.BigIntegerField(unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=20)),
                ('department', models.CharField(choices=[('CSE(R)', 'CSE(Regular)'), ('CSE(H)', 'CSE(HONORS)'), ('CSE&IT', 'CSIT')], max_length=50)),
                ('program', models.CharField(choices=[('B.TECH', 'B.TECH'), ('M.TECH', 'M.TECH')], max_length=50)),
                ('semester', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10)),
                ('year', models.IntegerField()),
                ('password', models.CharField(default='klu123', max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('contact', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'student_table',
            },
        ),
    ]
