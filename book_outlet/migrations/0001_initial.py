# Generated by Django 3.2.4 on 2021-07-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('rating', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
