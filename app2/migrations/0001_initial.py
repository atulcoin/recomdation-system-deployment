# Generated by Django 3.0.6 on 2020-10-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
            options={
                'db_table': 'Emp',
            },
        ),
        migrations.CreateModel(
            name='movieId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.ImageField(upload_to='')),
                ('titels', models.CharField(max_length=500)),
                ('geners', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'movie',
            },
        ),
    ]
