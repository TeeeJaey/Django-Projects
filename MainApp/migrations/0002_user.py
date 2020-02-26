# Generated by Django 2.2.5 on 2019-12-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=264)),
                ('lname', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]