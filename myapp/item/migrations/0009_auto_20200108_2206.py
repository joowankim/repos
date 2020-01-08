# Generated by Django 2.2.4 on 2020-01-08 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0008_auto_20200108_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('imgUrl', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Included',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('oily', models.IntegerField()),
                ('dry', models.IntegerField()),
                ('sensitive', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Thumbs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('imgUrl', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('imageId', models.TextField()),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('gender', models.TextField()),
                ('category', models.TextField()),
                ('ingredients', models.TextField()),
                ('monthlySales', models.IntegerField()),
                ('oily', models.IntegerField()),
                ('dry', models.IntegerField()),
                ('sensitive', models.IntegerField()),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='item.Images')),
                ('ingredient_ids', models.ManyToManyField(through='item.Included', to='item.Ingredient')),
                ('thumb', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='item.Thumbs')),
            ],
        ),
        migrations.AddField(
            model_name='included',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Ingredient'),
        ),
        migrations.AddField(
            model_name='included',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item'),
        ),
    ]
