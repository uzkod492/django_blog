# Generated by Django 4.1.3 on 2022-12-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_user_bio_user_image_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Izoh', 'verbose_name_plural': 'Izohlar'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Postlar'},
        ),
        migrations.AlterModelOptions(
            name='siteinfo',
            options={'verbose_name': 'Sayt haqida', 'verbose_name_plural': 'Sayt haqida'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Userlar'},
        ),
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
