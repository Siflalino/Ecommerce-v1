# Generated by Django 4.2.7 on 2024-03-01 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_commande_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-date_inscrit']},
        ),
        migrations.RemoveField(
            model_name='client',
            name='adress',
        ),
        migrations.AddField(
            model_name='client',
            name='adresse',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='client',
            name='date_inscrit',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='client',
            name='mot_de_passe',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='client',
            name='nom',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='pays',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='client',
            name='prenom',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='validé_mot_de_passe',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='ville',
            field=models.CharField(default='', max_length=300),
        ),
    ]
