# Generated by Django 4.2.7 on 2024-02-29 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_client_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=300)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('pays', models.CharField(max_length=300)),
                ('ville', models.CharField(max_length=300)),
                ('adresse', models.CharField(max_length=300)),
                ('date_commande', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_commande'],
            },
        ),
    ]
