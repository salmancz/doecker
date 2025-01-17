# Generated by Django 4.1 on 2022-08-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_gigi1a_appli_num"),
    ]

    operations = [
        migrations.CreateModel(
            name="GIGI1",
            fields=[
                ("Appli_num", models.AutoField(primary_key=True, serialize=False)),
                ("name_of_applicant", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                (
                    "persons_products_organization_authority",
                    models.CharField(max_length=100),
                ),
                ("type_of_goods", models.CharField(max_length=100)),
                ("specification", models.CharField(max_length=100)),
                ("name_of_geographical_indications", models.CharField(max_length=100)),
                ("desc_of_goods", models.CharField(max_length=100)),
                ("geo_area", models.CharField(max_length=100)),
                ("proof_of_origin", models.CharField(max_length=100)),
                ("method_of_production", models.CharField(max_length=100)),
                ("uniqueness", models.CharField(max_length=100)),
                ("inspection_body", models.CharField(max_length=100)),
                ("other", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=20)),
                ("is_deleted", models.BooleanField(default=False)),
                ("form_type", models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(name="GIGI1A",),
    ]
