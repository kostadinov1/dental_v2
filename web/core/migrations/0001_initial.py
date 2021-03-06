# Generated by Django 4.0.4 on 2022-05-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('1', 'Preventative'), ('2', 'Restorative'), ('3', 'Cosmetic')], max_length=30)),
                ('duration', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
