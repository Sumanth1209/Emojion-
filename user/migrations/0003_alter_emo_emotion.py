# Generated by Django 4.0.6 on 2022-10-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_emo_eu_alter_emo_emotion_alter_emo_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emo',
            name='emotion',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
