# Generated by Django 3.2.7 on 2021-09-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.FileField(blank=True, default='media/default.jpg', upload_to='media/'),
        ),
    ]
