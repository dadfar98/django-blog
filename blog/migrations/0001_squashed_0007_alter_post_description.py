# Generated by Django 4.2.3 on 2023-07-24 11:49

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('blog', '0001_initial'), ('blog', '0002_post_description_alter_post_slug'), ('blog', '0003_alter_post_description'), ('blog', '0004_post_image'), ('blog', '0005_alter_post_content'), ('blog', '0006_alter_post_title'), ('blog', '0007_alter_post_description')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('description', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('image', models.ImageField(default=None, upload_to='images')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]