# Generated by Django 3.0.3 on 2020-03-21 22:03

import dashboard.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200314_1453'),
        ('dashboard', '0013_auto_20190817_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemesterDownloadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, help_text='Optional description of the file', max_length=250)),
                ('content', models.FileField(help_text='The file itself', upload_to=dashboard.models.download_file_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'tex', 'png', 'jpg'])])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('semester', models.ForeignKey(help_text='The semester to which the file is associated', on_delete=django.db.models.deletion.CASCADE, to='core.Semester')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
