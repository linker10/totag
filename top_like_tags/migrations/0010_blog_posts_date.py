# Generated by Django 3.0.7 on 2020-07-21 12:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('top_like_tags', '0009_about_contact_page_hashtag_tips_home_most_popular_hashtags_policy_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_posts',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 7, 21, 12, 20, 9, 763133, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
