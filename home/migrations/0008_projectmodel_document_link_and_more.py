# Generated by Django 5.0.7 on 2024-08-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homebuttonmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='document_link',
            field=models.FileField(blank=True, default=None, null=True, upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='demo_link',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='github_link',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
