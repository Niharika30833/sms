# Generated by Django 5.0 on 2024-02-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0005_alter_signin_id_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.CharField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='signin',
            name='id',
            field=models.CharField(primary_key=True, serialize=False),
        ),
    ]