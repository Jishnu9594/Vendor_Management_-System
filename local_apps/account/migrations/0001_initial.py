# Generated by Django 4.1.13 on 2024-05-01 07:11

from django.db import migrations, models
import local_apps.account.managers
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("prefix", models.CharField(default="SA", max_length=10)),
                ("first_two_letters", models.CharField(default="AA", max_length=2)),
                ("first_two_numbers", models.IntegerField(default=0)),
                ("last_one_letter", models.CharField(default="A", max_length=1)),
                ("last_two_numbers", models.IntegerField(default=0)),
                ("account_id", models.CharField(max_length=220)),
                ("is_email_verified", models.BooleanField(default=False)),
                ("is_mobile_verified", models.BooleanField(default=False)),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "A user with that email already exists."
                        },
                        max_length=200,
                        unique=True,
                    ),
                ),
                (
                    "mobile",
                    models.CharField(
                        blank=True,
                        error_messages={
                            "unique": "A user with that mobile already exists."
                        },
                        max_length=20,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Admin", "Admin"),
                            ("Staff", "Staff"),
                            ("Vendor", "Vendor"),
                            ("User", "User"),
                            ("Others", "Others"),
                        ],
                        default="Others",
                        help_text="ID generation depends on the role. Once you submit it will be permanent.",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "ordering": ["-created_at", "-updated_at"],
            },
            managers=[
                ("objects", local_apps.account.managers.CustomUserManager()),
            ],
        ),
    ]