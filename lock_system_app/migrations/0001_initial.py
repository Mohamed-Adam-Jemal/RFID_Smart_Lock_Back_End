# Generated by Django 5.1.3 on 2024-11-30 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RFIDUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('rfid_tag', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lock_system_app.rfiduser')),
            ],
        ),
    ]
