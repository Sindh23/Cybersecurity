# Generated by Django 3.0 on 2024-05-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_sendquery_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendquery',
            name='transid',
            field=models.CharField(default=100, max_length=10),
            preserve_default=False,
        ),
    ]
