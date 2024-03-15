from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'delEscolha2', views.delEscolha2, name='delEscolha2'),
    url(r'escolha_eletiva', views.escolha_eletiva, name='escolha_eletiva'),
    url(r'sair', views.sair, name='sair'),
    url(r'importe_aluno', views.importe_aluno, name='importe_aluno'),
    url(r'loginEscola', views.loginEscola, name='loginEscola'),
    url(r'cadastroEletiva', views.cadastroEletiva, name='cadastroEletiva'),
    url(r'consultaAlunos', views.consultaAlunos, name='consultaAlunos'),
    url(r'consultaEletiva', views.consultaEletiva, name='consultaEletiva'),
    url(r'delAluno/(?P<cod>[0-9]+)/', views.delAluno, name='delAluno'),
    url(r'delCadastro/(?P<cod>[0-9]+)/', views.delCadastro, name='delCadastro'),
    url(r'consultaCadastro/(?P<cod>[0-9]+)/', views.consultaCadastro, name='consultaCadastro'),
    url(r'^$', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
