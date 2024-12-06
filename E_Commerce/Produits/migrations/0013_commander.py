# Generated by Django 5.1.3 on 2024-11-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produits', '0012_categories_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commander',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('addresse', models.CharField(max_length=200)),
                ('telephone', models.IntegerField()),
                ('notes', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('items', models.CharField(max_length=600)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]