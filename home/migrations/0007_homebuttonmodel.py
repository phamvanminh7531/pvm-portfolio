# Generated by Django 5.0.7 on 2024-08-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_achievementmodel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeButtonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_title', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
