# Generated by Django 2.2.5 on 2019-12-29 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topName', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
                ('topic', models.ForeignKey(on_delete=True, to='MyDjangoApp.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=True, to='MyDjangoApp.Webpage')),
            ],
        ),
    ]
