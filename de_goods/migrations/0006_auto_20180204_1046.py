# Generated by Django 2.0.1 on 2018-02-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('de_goods', '0005_goodimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeinfo',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='typeinfo',
            name='turl',
            field=models.CharField(default='', max_length=64),
        ),
    ]