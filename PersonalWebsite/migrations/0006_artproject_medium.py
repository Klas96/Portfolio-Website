# Generated by Django 5.1.4 on 2025-01-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalWebsite', '0005_delete_certificate_delete_personaldescription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artproject',
            name='medium',
            field=models.CharField(blank=True, choices=[('DIGITAL', 'Digital'), ('SKETCH', 'Sketch'), ('PASTEL', 'Pastel')], max_length=255, null=True),
        ),
    ]
