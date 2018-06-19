# Generated by Django 2.0.6 on 2018-06-18 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=30, unique=True)),
                ('passcode', models.CharField(max_length=20)),
                ('submition_datetime', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('status', models.IntegerField(choices=[(0, 'Not reviewed'), (1, 'Accepted'), (2, 'Declined')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('case_script', models.FileField(upload_to='scripts/')),
            ],
        ),
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='documents/')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Case')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.DocumentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('ARCHIVE', 'Archive'), ('OFFICE', 'Office')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaperDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Case')),
                ('locker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Locker')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.DocumentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='case',
            name='checkpoint',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='api.Checkpoint'),
        ),
        migrations.AddField(
            model_name='case',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Employee'),
        ),
        migrations.AddField(
            model_name='case',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.CaseType'),
        ),
    ]
