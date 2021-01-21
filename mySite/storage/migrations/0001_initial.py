# Generated by Django 3.1.5 on 2021-01-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.FileField(upload_to='storage/')),
                ('flow_count', models.CharField(max_length=16, verbose_name='Number of flows')),
                ('packet_count', models.CharField(max_length=16, verbose_name='Number of Packets')),
                ('size', models.CharField(max_length=16, verbose_name='Size (MB)')),
            ],
        ),
    ]
