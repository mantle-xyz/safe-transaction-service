# Generated by Django 4.2.5 on 2023-10-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0075_multisigtransaction_proposer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="safemastercopy",
            name="deployer",
            field=models.CharField(default="Safe", max_length=50),
        ),
    ]