# Generated by Django 5.0.7 on 2024-07-30 16:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechUsedTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('github_link', models.URLField(blank=True, null=True)),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('tech_used_tag', models.ManyToManyField(to='home.techusedtagmodel')),
            ],
        ),
    ]
