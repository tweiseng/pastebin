# Generated by Django 2.0.6 on 2018-06-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paste_name', models.CharField(max_length=200)),
                ('paste_content', models.TextField()),
                ('paste_url', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('date_of_expiry', models.DateTimeField()),
            ],
        ),
    ]