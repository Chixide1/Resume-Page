# Generated by Django 5.0.1 on 2024-03-09 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_certifications_projects_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='link',
            field=models.URLField(),
        ),
    ]
