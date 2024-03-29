# Generated by Django 2.0 on 2024-02-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroAluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=30)),
                ('nome', models.CharField(max_length=100)),
                ('nascimento', models.CharField(max_length=30)),
                ('serie', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CadastroEletiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProf', models.CharField(max_length=100)),
                ('nomeEletiva', models.CharField(max_length=100)),
                ('anoSerie', models.CharField(max_length=30)),
                ('qntVagas', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EletivaAluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=30)),
                ('eletiva', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Cadastro',
        ),
    ]
