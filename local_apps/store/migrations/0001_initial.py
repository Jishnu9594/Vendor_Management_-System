# Generated by Django 4.1.13 on 2024-05-01 11:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("contact_details", models.TextField(blank=True, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "vendor_code",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("on_time_delivery_rate", models.FloatField(blank=True, null=True)),
                ("quality_rating_avg", models.FloatField(blank=True, null=True)),
                ("average_response_time", models.FloatField(blank=True, null=True)),
                ("fulfillment_rate", models.FloatField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("po_number", models.CharField(blank=True, max_length=255, null=True)),
                ("order_date", models.DateTimeField(blank=True, null=True)),
                ("delivery_date", models.DateTimeField(blank=True, null=True)),
                ("items", models.JSONField(blank=True, null=True)),
                ("quantity", models.IntegerField(blank=True, null=True)),
                ("status", models.CharField(blank=True, max_length=255, null=True)),
                ("quality_rating", models.FloatField(blank=True, null=True)),
                ("issue_date", models.DateTimeField(blank=True, null=True)),
                ("acknowledgment_date", models.DateTimeField(blank=True, null=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="store_purchase_order_vendor",
                        to="store.vendor",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HistoricalPerformance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateTimeField(blank=True, null=True)),
                ("on_time_delivery_rate", models.FloatField(blank=True, null=True)),
                ("quality_rating_avg", models.FloatField(blank=True, null=True)),
                ("average_response_time", models.FloatField(blank=True, null=True)),
                ("fulfillment_rate", models.FloatField(blank=True, null=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="store_historical_performance_vendor",
                        to="store.vendor",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
