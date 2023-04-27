# Generated by Django 3.2.18 on 2023-04-27 07:54

import django.db.models.deletion
from django.db import migrations, models

import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0057_updated_homepage_video_block"),
        ("roadmap", "0004_auto_20230426_1220"),
    ]

    operations = [
        migrations.AddField(
            model_name="roadmappage",
            name="fine_print",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="roadmappage",
            name="sponsorship_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.contentpage",
            ),
        ),
    ]
