import pandas as pd
import numpy as np
import random
import string
from classes import *

def random_string_generator(str_size):
    """
        Função que gera uma string aleatória
        :param str_size: tamanho da string
        :return: retorna a string gerada
    """
    return ''.join(random.choice(string.ascii_letters) for x in range(str_size))

def createSetorEconomico():
    """
        Funcão que instancia um setor economico
        :return: uma instância de um SetorEconomico
    """
    return setorEconomico(
        np.random.randint(50,100),
        np.random.randint(10),
        np.random.randint(10), 
        0)

def createSetorMilitar():
    """
        Funcão que instancia um setor Militar
        :return: uma instância de um SetorMilitar
    """
    bombas = ['BP','BM','BG']
    combatentes = ['Soldado','Tanque','Jipe']
    arsenal = pd.Series({bomba:np.random.randint(100) for bomba in bombas})
    tropa = pd.Series({comb:np.random.randint(1000) for comb in combatentes})
    
    return setorMilitar(arsenal, tropa)

def createSetorPrivado():
    """
        Funcão que instancia um setor Privado
        :return: uma instância de um SetorPrivado
    """
    produtos = ['P1','P2','P3','P4','P5']
    
    estoque  = pd.Series({prod:np.random.randint(100) for prod in produtos})
    producao = pd.Series(np.random.randint(0,6,size = 5), index = produtos)
    
    importacao = pd.Series([0 for i in range(len(produtos))], index = produtos)
    exportacao = pd.Series([0 for i in range(len(produtos))], index = produtos)
    
    return setorPrivado(estoque, producao, importacao, exportacao)

def createLider():
    """
        Funcão que instancia um Lider
        :return: uma instância de um Lider
    """
    nome = random_string_generator(10)
    orientacao = random.choice([-1,0,1])
    
    return Lider(nome,orientacao)

def createPais(nome, mundo):
    """
        Funcão que instancia um Pais
        :param nome: nome do país
        :param mundo: endereço para a instância do mundo
        :return: uma instância de um País
    """
    continente = random.choice(['C1','C2','C3'])
        setorEconomico = createSetorEconomico()
        setorMilitar = createSetorMilitar()
        setorPrivado = createSetorPrivado()
        lider = createLider()
        
        return Pais(nome, populacao, imigrantes, 
        continente, setorEconomico, setorMilitar, 
        setorPrivado, lider, mundo)
   
def createInteracaoFixa(mundo):
    """
        Funcão que instancia uma InteracaoFixa
        :param mundo: endereço para uma instância do mundo
        :return: uma instância de uma InteracaoFixa
    """
    escolhida = random.choice([InteracaoMilitar, InteracaoPrivada, InteracaoEconomica])
    paises = mundo.paisesAleatorios() # Remover jogador desse conjunto
    inicio = mundo.ano
    vigencia = np.random.randint(1,20)
    fator = np.random.rand()
    
    interacao = escolhida(paises, inicio, vigencia, fator)
    mundo.interacoesFixas.append(interacao)
    
    return interacao


def createAcaoAleatoria(mundo):
    """
    Cria e executa ação aleatória
    :param mundo:
    :return:
    """
    ator = random.choice(mundo.paises)
    alvo = random.choice(mundo.paises)
    fator = np.random.rand()
    nomePanorama = random.choice(['militar','privado','economico'])
    AcaoAleatoria = Acao('Acao Repentina',ator, nomePanorama)
    AcaoAleatoria.fazerEfeito(alvo, fator)
