# Generated by Django 3.0.8 on 2020-07-09 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_name', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
