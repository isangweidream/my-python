# Generated by Django 2.0.1 on 2018-02-03 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('de_goods', '0004_typeinfo_pid'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lbsm', models.CharField(default='', max_length=10)),
                ('sbpic', models.ImageField(upload_to='de_goods')),
                ('lbpic', models.ImageField(upload_to='de_goods')),
                ('gid', models.ForeignKey(on_delete=None, to='de_goods.GoodInfo')),
            ],
        ),
    ]