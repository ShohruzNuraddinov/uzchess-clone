# Generated by Django 4.2.8 on 2023-12-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_image_alter_news_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/news/'),
        ),
    ]
