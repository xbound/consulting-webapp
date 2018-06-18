# Generated by Django 2.0.6 on 2018-06-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_case_is_declined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='is_accepted',
        ),
        migrations.RemoveField(
            model_name='case',
            name='is_declined',
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[(0, 'N/A'), (1, 'ACCEPTED'), (2, 'DECLINED')], default=0, max_length=30),
        ),
    ]
