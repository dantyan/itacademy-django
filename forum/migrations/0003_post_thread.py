# Generated by Django 2.1.7 on 2019-02-13 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_thread_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
        ),
    ]
