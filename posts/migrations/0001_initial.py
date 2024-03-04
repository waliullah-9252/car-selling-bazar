# Generated by Django 4.2.7 on 2023-12-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/media/uploads/')),
                ('car_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=None)),
                ('price', models.CharField(max_length=100)),
                ('buy_now', models.CharField(max_length=100)),
                ('brand_name', models.ManyToManyField(to='brands.brandmodel')),
            ],
        ),
    ]
