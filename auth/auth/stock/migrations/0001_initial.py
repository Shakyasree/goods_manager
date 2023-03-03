# Generated by Django 4.0.6 on 2022-09-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=100)),
                ('squantity', models.IntegerField()),
            ],
            options={
                'db_table': 'stock',
            },
        ),
    ]
