# Generated by Django 4.2.6 on 2023-10-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_link',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_link',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(max_length=50, null=True),
        ),
    ]
