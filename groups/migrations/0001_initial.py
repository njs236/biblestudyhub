# Generated by Django 3.0.4 on 2020-03-28 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudySession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('meeting_link', models.CharField(max_length=300)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
            ],
        ),
    ]