# Generated by Django 3.2.6 on 2021-09-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time', models.PositiveIntegerField(default=0)),
                ('username', models.CharField(default='Anonymous', max_length=18)),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
