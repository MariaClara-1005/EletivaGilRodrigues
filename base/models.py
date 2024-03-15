from django.db import models

class CadastroAluno(models.Model):
    matricula = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=30)
    serie = models.CharField(max_length=30)
    turma = models.CharField(max_length=50, null=True)
    eletiva1 = models.CharField(max_length=50, null=True)
    eletiva2 = models.CharField(max_length=50, null=True)

class CadastroEletiva(models.Model):
    nomeProf = models.CharField(max_length=100)
    nomeEletiva = models.CharField(max_length=100)
    anoSerie = models.CharField(max_length=30)
    qntVagas = models.CharField(max_length=10)
    bloco = models.CharField(max_length=30, null=True)

class Arq(models.Model):
	arq = models.FileField()
     

