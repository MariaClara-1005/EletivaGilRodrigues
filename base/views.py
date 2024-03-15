from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def delEscolha2(request):
    matricula = request.user.username
    historico = CadastroEletiva.objects.all()
    eletiva = CadastroAluno.objects.filter(matricula=matricula)

    for h in historico:
        for e in eletiva:
            if h.nomeEletiva == e.eletiva1:
                vagas = int(h.qntVagas)
                cc = int(h.id)
                CadastroEletiva.objects.filter(id=cc).update(qntVagas = vagas + 1)
                CadastroAluno.objects.filter(matricula=matricula).update(eletiva1 = 'None')

            if h.nomeEletiva == e.eletiva2:
                vagas = int(h.qntVagas)
                cc = int(h.id)
                CadastroEletiva.objects.filter(id=cc).update(qntVagas = vagas + 1)
                CadastroAluno.objects.filter(matricula=matricula).update(eletiva2 = 'None')
    return redirect(escolha_eletiva)

@login_required
def escolha_eletiva(request):
    matricula = request.user.username
    eletiva = CadastroEletiva.objects.all()
    alunos = CadastroAluno.objects.filter(matricula=matricula)
    if request.method == "POST":
        matricula = matricula
        eletiva1 = request.POST.get('eletiva1')
        eletiva2 = request.POST.get('eletiva2')
        CadastroAluno.objects.filter(matricula=matricula).update(eletiva1 = eletiva1, eletiva2=eletiva2)
        for e in eletiva:
            for a in alunos:
                if e.nomeEletiva == a.eletiva1:
                    vagas = int(e.qntVagas)
                    cc = int(e.id)
                    CadastroEletiva.objects.filter(id=cc).update(qntVagas = vagas - 1)
            if e.nomeEletiva == a.eletiva2:
                    vagas = int(e.qntVagas)
                    cc = int(e.id)
                    CadastroEletiva.objects.filter(id=cc).update(qntVagas = vagas - 1)
        return redirect(escolha_eletiva)
    return render(request, 'escolha_eletiva.html', {'eletiva': eletiva, 'alunos': alunos})     


@login_required
def sair(request):
    logout(request)
    return redirect(home)

def home (request):
    #Cria usuarios
    #for c in CadastroAluno.objects.all():
    #    us = User.objects.create_user(str(c.matricula), '', str(c.nascimento))
    #    us.first_name = '1'
    #    us.save()
    
    #se o metodo do html for POST
    if request.method == "POST":
        #captura usuario digitato no input com o name 'usuario'
        usuario = request.POST.get('usuario')
        #captura senha digitata no input com o name 'senha'
        senha = request.POST.get('senha')
        #autentica se realmente a senha e login esta certo, lembrando que tem que importar 'from django.contrib.auth import authenticate'
        usu = authenticate(username=usuario, password=senha)
        #Se tiver tudo certinho com o usuario
        if usu is not None:
            #consulta o usuario
            us = User.objects.filter(username=usuario)
            for u in us:
                #verifica o nivel de acesso
                if u.first_name == "1":
                    login(request, usu)
                    return redirect(escolha_eletiva)
                else:
                    #significa que o acesso e diferente e vai pra outra pagina
                    
                    pass
        else:
            return render(request, 'index.html', {'msg': "Falha!"})
    return render(request, 'index.html')

def loginEscola(request):
      #Cria usuario
    '''us = User.objects.create_user('secretaria', 'dsetegilrodrigues@gmail.com', '@melhordev')
    us.first_name = '1'
    us.save()'''
    #se o metodo do html for POST
    if request.method == "POST":
        #captura usuario digitato no input com o name 'usuario'
        usuario = request.POST.get('usuario')
        #captura senha digitata no input com o name 'senha'
        senha = request.POST.get('senha')
        #autentica se realmente a senha e login esta certo, lembrando que tem que importar 'from django.contrib.auth import authenticate'
        usu = authenticate(username=usuario, password=senha)
        #Se tiver tudo certinho com o usuario
        if usu is not None:
            #consulta o usuario
            us = User.objects.filter(username=usuario)
            for u in us:
                #verifica o nivel de acesso
                if u.first_name == "1":
                    login(request, usu)
                    return redirect(consultaEletiva)
                else:
                    #significa que o acesso e diferente e vai pra outra pagina
                    
                    pass
        else:
            return render(request, 'loginEscola.html', {'msg': "Falha!"})
    return render(request, 'loginEscola.html', {'msg': ''})

@login_required
def consultaAlunos(request):
    #CadastroAluno.objects.all().delete()
    cadastro = CadastroAluno.objects.all().order_by('nome')
    return render(request, 'consultaAlunos.html', {'cadastro': cadastro})

@login_required
def cadastroEletiva(request):
    if request.method == "POST":
        nomeProf = request.POST.get('nomeProf')
        nomeEletiva = request.POST.get('nomeEletiva')
        anoSerie = request.POST.get('anoSerie')
        qntVagas = request.POST.get('qntVagas')
        bloco = request.POST.get('bloco')
        CadastroEletiva(nomeProf=nomeProf, nomeEletiva=nomeEletiva, 
                        anoSerie=anoSerie, qntVagas=qntVagas, bloco=bloco).save()
    return render(request, 'cadastro_eletiva.html')

@login_required
def consultaEletiva(request):
    cadastro = CadastroEletiva.objects.all()
    return render(request, 'consultaEletivas.html', {'cadastro': cadastro})

def delCadastro(request, cod):
    CadastroEletiva.objects.filter(id=cod).delete()
    return redirect(consultaEletiva)

def delAluno(request, cod):
    CadastroAluno.objects.filter(id=cod).delete()
    return redirect(consultaAlunos)

@login_required
def consultaCadastro(request, cod):
    cadastro = CadastroEletiva.objects.filter(id=cod)
    return render(request, 'consultaCadastro.html', {'cadastro': cadastro})


def importe_aluno(request):
    #Arq.objects.all().delete()
    #CadastroAluno.objects.all().delete()
    if request.method == "POST":

        anexo = request.FILES.get('anexo')

        arq = Arq(arq=anexo)
        arq.save()

        arq = open('/home/maria_clara/Área de Trabalho/eletiva/base/static/media/' + str(anexo), 'r')
        x = 0
        ar = arq.readlines()
        for a in ar:
            if x == 0 :
                x = 1
            else:
                try:   
                    CadastroAluno(matricula =str(a).split(";")[0],
                        nome =str(a).split(";")[1],
                        nascimento = str(a).split(";")[2],
                        serie = str(a).split(";")[3],
                        turma = str(a).split(";")[4]).save()
                except Exception as ex:
                    print(ex)

    return render(request, 'importe_aluno.html')
