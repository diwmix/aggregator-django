# Generated by Django 4.2 on 2024-03-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0003_alter_university_img_alter_university_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='accreditationLevel',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='university',
            name='contactInfo',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='features',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='img',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='university',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='university',
            name='rating',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='remoteEducation',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='reviews',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='specialties',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='university',
            name='universityName',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='website',
            field=models.CharField(blank=True),
        ),
    ]