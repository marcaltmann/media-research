# Generated by Django 5.0.3 on 2024-03-12 20:47

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gnd_id', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('D', 'Diverse'), ('N', 'Not specified')], default='N', max_length=1)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gnd_id', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='archive',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='interview',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='interview',
            name='media_type',
            field=models.CharField(default='video/mp4', max_length=100),
        ),
        migrations.AddField(
            model_name='interview',
            name='media_url',
            field=models.URLField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='interview',
            name='poster',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='interview',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.CreateModel(
            name='InterviewInvolvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('INT', 'Interviewee'), ('ITR', 'Interviewer'), ('CAM', 'Camera'), ('SND', 'Sound'), ('EDT', 'Editor'), ('OTH', 'Other')], default='INT', max_length=3)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.interview')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.person')),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='people',
            field=models.ManyToManyField(through='archive.InterviewInvolvement', to='archive.person'),
        ),
        migrations.CreateModel(
            name='TopicReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timecode', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.interview')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.topic')),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='topics',
            field=models.ManyToManyField(through='archive.TopicReference', to='archive.topic'),
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.JSONField()),
                ('vtt', models.TextField()),
                ('language', models.CharField(max_length=5)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.interview')),
            ],
        ),
    ]
