# Generated by Django 2.0.5 on 2018-05-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TopicCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_english', models.CharField(max_length=100)),
                ('title_other', models.CharField(max_length=100)),
                ('short_description', models.TextField(max_length=200)),
                ('image_name', models.CharField(max_length=50)),
            ],
        ),
    ]
