# Generated by Django 4.2.5 on 2024-07-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_aianalysislog_confidence_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aianalysislog",
            name="request_timestamp",
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="aianalysislog",
            name="response_timestamp",
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="aianalysislog",
            name="returnclass",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
