# Generated by Django 4.2.1 on 2023-05-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('TestId', models.AutoField(primary_key=True, serialize=False)),
                ('TestName', models.CharField(max_length=400)),
            ],
        ),
    ]
