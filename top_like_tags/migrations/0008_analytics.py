# Generated by Django 3.0.6 on 2020-06-10 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_like_tags', '0007_auto_20200531_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_page', models.IntegerField()),
                ('popular_hashtag', models.IntegerField()),
                ('forums', models.IntegerField()),
                ('full_blog', models.IntegerField()),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
