# Generated by Django 3.0.3 on 2020-07-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('createTime', models.DateField(auto_now_add=True)),
                ('modifyTime', models.DateField(auto_now=True)),
            ],
        ),
    ]
