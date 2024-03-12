# Generated by Django 4.2 on 2024-03-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('imageUrl', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
