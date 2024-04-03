# Generated by Django 3.2.12 on 2022-03-30 09:25

from django.db import migrations, models

import safe_transaction_service.history.models


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0057_alter_webhook_authorization"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webhook",
            name="url",
            field=models.CharField(
                max_length=255,
                validators=[
                    safe_transaction_service.history.models._validate_webhook_url
                ],
            ),
        ),
    ]
