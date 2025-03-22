# Generated by Django 5.1.7 on 2025-03-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('batch', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('skills', models.TextField()),
                ('experience', models.TextField()),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, null=True)),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile_pics/')),
            ],
        ),
    ]
