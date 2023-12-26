# Generated by Django 4.2.8 on 2023-12-20 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=256)),
                ('about', models.TextField()),
                ('dis_price', models.FloatField()),
                ('price', models.FloatField()),
                ('rating', models.FloatField(default=0)),
                ('level', models.CharField(choices=[('Starter', 'Starter'), ('Professional', 'Professional'), ('Amateur', 'Amateur')], max_length=128)),
                ('lang', models.CharField(choices=[('uz', 'Uzbek'), ('en', 'English'), ('ru', 'Russian')], max_length=128)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='book/pic/')),
                ('published_at', models.IntegerField()),
                ('page_count', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.bookauthor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.bookcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]