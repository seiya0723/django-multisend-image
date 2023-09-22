# Generated by Django 4.2.5 on 2023-09-22 14:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('comment', models.CharField(max_length=2000, verbose_name='コメント')),
            ],
        ),
        migrations.CreateModel(
            name='TopicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('content', models.ImageField(upload_to='bbs/topic_image/content', verbose_name='画像')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.topic', verbose_name='トピック')),
            ],
        ),
    ]