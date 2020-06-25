import numpy as np
import pandas as pd
import random
from random import randint

##SISTEMA SEGURO##
###############################################################
class Mundo():
    """
        Classe onde todos os outros objetos vão residir. Vai ser usada majoritariamente como um hub de informações.
    """
    def __init__(self):
        """
            A classe é instanciada sem nenhum atributo porque eles são instaciados depois, recebendo Mundo() como attr.
        """
        self.__paises = {} # é um dicionário no formato {'nome_pais':Pais()}
        self.__ano = 1 # Variável de contagem de turnos
        self.__interacoesFixas = [] # Lista com os objetos interacaoFixa()
        self.__panorama = None # Panorama() do mundo, com os três filhos
        self.__jogador = None

    @property
    def paises(self):
        return self.__paises
        
    @paises.setter
    def paises(self, paises):
        self.__paises = paises

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def interacoesFixas(self):
        return self.__interacoesFixas

    @interacoesFixas.setter
    def interacoesFixas(self, interacoesFixas):
        self.__interacoesFixas = interacoesFixas
    
    @property
    def panorama(self):
        return self.__panorama

    @panorama.setter
    def panorama(self, panorama):
        self.__panorama = panorama

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador
    

    
    def paisesAleatorios(self, n_paises=None):
        """
            Método a ser usado para gerar interacaoFixa() aleatórias.
            :param n_paises: (opcional) Numero preciso de países contidos. Se omitido, escolhe-se um número aleatório
            entre 2 e o número de países.
            :return: Dicionário no formato {'nome_pais':Pais()} contendo n_paises chaves.
        """
        if len(self.paises) <= 2:
            # Exceção para caso esteja vazio ou com menos países do que o necessário
            raise Exception('O mundo nem país tem. Resolve isso primeiro.')

        if n_paises is None:
            n_paises = np.random.randint(2, len(self.paises))

        nomesAleatorios = set()

        while len(nomesAleatorios) < n_paises:
            nomesAleatorios.add(random.choice([x for x in self.paises.keys()]))

        nomesAleatorios = sorted(list(nomesAleatorios))

        nomesAleatorios = {pais: self.paises[pais] for pais in nomesAleatorios}

        return nomesAleatorios

    def mostrarPanorama(self):

        print(self.panorama.geral)

        
##############################################################
class Panorama():
    """
        Classe que representa os panoramas do Mundo, ou seja a relação de cada 
        país com outro em cada esfera(Privada, Militar e Econômica)    
    """
    def __init__(self, mundo):
        """
            :param mundo: recebe o endereço de uma instância da classe Mundo (Mundo)
        """
        # Teste para não ter países
        if len(mundo.paises) == 0:
            raise Exception('Que mundo fraco! Tem nem país')

        listaDePaises = mundo.paises.keys()
        n_paises = len(listaDePaises)

        self.__economico = pd.DataFrame(np.random.rand(n_paises, n_paises), index=listaDePaises, columns=listaDePaises)
        self.__privado = pd.DataFrame(np.random.rand(n_paises, n_paises), index=listaDePaises, columns=listaDePaises)
        self.__militar = pd.DataFrame(np.random.rand(n_paises, n_paises), index=listaDePaises, columns=listaDePaises) 

        self.__geral = self.__economico + self.__privado + self.__militar

    def __repr__(self):
        return "Panorama geral:\n" + self.__geral.to_string()

    @property
    def economico(self):
        return self.__economico

    @economico.setter
    def economico(self, economico):
        self.__economico = economico

    @property
    def privado(self):
        return self.__privado

    @privado.setter
    def privado(self, privado):
        self.__privado = privado

    @property
    def militar(self):
        return self.__militar

    @militar.setter
    def militar(self, militar):
        self.__militar = militar

    @property
    def geral(self):
        return self.__geral

    @geral.setter
    def geral(self, geral):
        self.__geral = geral


    def atualizarPanorama(self):
        """
            Função chamada para atualizar os valores do panorama geral
            :return: retorna o panorama geral
        """
        self.geral = self.economico + self.privado + self.militar

        return self.geral

    def alterarRelacao(self, A, B, nomePanorama, fator):
        """
            Função chamada para alterar a relação de determinados países em determinado panorama 
            :param A: Um dos países da relação (Pais)
            :param B: Outro dos países da relação (Pais)
            :param nomePanorama: indica qual o panorama a ser alterado (str)
            :param fator: indica o fator que será adicionado ou subtraído na relação (float)
        """

        if nomePanorama == 'militar':
            self.militar.loc[A.nome, B.nome] = self.militar.loc[A.nome, B.nome] + fator
            self.militar.loc[B.nome, A.nome] = self.militar.loc[B.nome, A.nome] + fator

            self.atualizarPanorama()

        if nomePanorama == 'privado':
            self.privado.loc[A.nome, B.nome] = self.privado.loc[A.nome, B.nome] + fator
            self.privado.loc[B.nome, A.nome] = self.privado.loc[B.nome,A.nome] + fator

            self.atualizarPanorama()

        if nomePanorama == 'economico':
            self.economico.loc[A.nome, B.nome] = self.economico.loc[A.nome, B.nome] + fator
            self.economico.loc[B.nome, A.nome] = self.economico.loc[B.nome,A.nome] + fator

            self.atualizarPanorama()

##############################################################
class Pais():
    """
        Classe que representa um país. Será atribuido a um jogador
    """
    def __init__(self, nome, continente,
    setorEconomico, setorMilitar, setorPrivado, 
    lider, mundo):
        """
            :param nome: Nome do país (str)
            :param populacao: população do país (int)
            :param imigrantes: quantidade de imigrantes (int) 
            :param continente: continente em que o país se encontra (str)
            :param setorEconomico: endereço para uma instância de classe com as características econômicas (SetorEconomico)
            :param setorMilitar: endereço para uma instância de classe com as características econômicas (SetorMilitar)
            :param setorPrivado: endereço para uma instância de classe com as características econômicas (SetorPrivado)
            :param lider: endereço para uma instância de classe com as carcterística do líder (Lider)
            :param mundo: enderço para uma instância da classe que representa o mundo (Mundo)
        """
        self.__nome = nome
        self.__continente = continente
        self.__setorEconomico = setorEconomico
        self.__setorMilitar = setorMilitar
        self.__setorPrivado = setorPrivado
        self.__lider = lider
        self.__mundo = mundo

        # print(f'Criei o pais {nome}')

        if self.__nome in self.mundo.paises:
            Exception('Esse país já existe cara!')

        self.mundo.paises[self.nome] = self #se adiciona na lista de países do mundo

    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def continente(self):
        return self.__continente
    
    @continente.setter
    def continente(self, continente):
        self.__continente = continente
    
    @property
    def setorEconomico(self):
        return self.__setorEconomico
    
    @setorEconomico.setter
    def setorEconomico(self, setorEconomico):
        self.__setorEconomico = setorEconomico
    
    @property
    def setorMilitar(self):
        return self.__setorMilitar
    
    @setorMilitar.setter
    def setorMilitar(self, setorMilitar):
        self.__setorMilitar = setorMilitar
    
    @property
    def setorPrivado(self):
        return self.__setorPrivado
    
    @setorPrivado.setter
    def setorPrivado(self, setorPrivado):
        self.__setorPrivado = setorPrivado
    
    @property
    def lider(self):
        return self.__lider
    
    @lider.setter
    def lider(self, lider):
        self.__lider = lider
    
    @property
    def mundo(self):
        return self.__mundo
    
    @mundo.setter
    def mundo(self, mundo):
        self.__mundo = mundo
    

##############################################################

class Jogador(Pais):
    """
    Pais 'superpoderoso', com os métodos de jogador
    """
    def __init__(self, nome, continente,
    setorEconomico, setorMilitar, setorPrivado,
    lider, mundo):
        super().__init__(nome, continente,
    setorEconomico, setorMilitar, setorPrivado,
    lider, mundo)
        self.__acoesDeJogador = {1:{1:Acao('Acao A1',self,'economico'),
                                            2:Acao('Acao A2',self, 'economico')},
                               2:{1:Acao('Acao M1',self,'militar'),
                                            2:Acao('Acao M2',self, 'militar')},
                               3:{1:Acao('Acao P1',self,'privado'),
                                            2:Acao('Acao P2',self, 'privado')}}
        self.mundo.jogador = self
        self.objetivo = randint(4,10)
        self.pais_objetivo = random.choice(['A','B','C','D','E','F'])

        print(f'\nSeu objetivo é alcançar {self.objetivo} pontos com o país {self.pais_objetivo}')
    @property
    def acoesDeJogador(self):
       return self.__acoesDeJogador

    @acoesDeJogador.setter
    def acoesDeJogador(self, acoesDeJogador):
        self.__acoesDeJogador = acoesDeJogador

    def cumpriuObjetivo(self):
        if self.objetivo is None:
            raise Exception('Não tem objetivo ainda')
        else:
            return self.mundo.panorama.geral.loc[self.nome,self.pais_objetivo] >= self.objetivo
##############################################################
class SetorEconomico():
    """
        Classe que comporta informações sobre o setor econômico de um país
    """
    def __init__(self, limite_aReceber, limite_aPagar):
        """
            :param limite_aReceber: limite de investimento que um pais pode receber (float)
            :param limite_aPagar: limite de investimento que um pais pode dar (float)
        """
        self.__limite_aReceber = limite_aReceber
        self.__limite_aPagar = limite_aPagar
        
        self.__aPagar = pd.Series(dtype = float)
        self.__aReceber = pd.Series(dtype = float)

    @property
    def limite_aPagar(self):
        return self.__limite_aPagar

    @limite_aPagar.setter
    def limite_aPagar(self, limite_aPagar):
        self.__limite_aPagar = limite_aPagar

    @property
    def limite_aReceber(self):
        return self.__limite_aReceber

    @limite_aReceber.setter
    def limite_aReceber(self, limite_aReceber):
        self.__limite_aReceber = limite_aReceber

    @property
    def aPagar(self):
        return self.__aPagar

    @aPagar.setter
    def aPagar(self, aPagar):
        self.__aPagar = aPagar

    @property
    def aReceber(self):
        return self.__aReceber

    @aReceber.setter
    def aReceber(self, aReceber):
        self.__aReceber = aReceber
        
##############################################################
class SetorMilitar():
    """
        Classe que comporta informações sobre o setor militar de um país
    """
    def __init__(self, arsenal, tropa):
        """
            :param arsenal: informações sobre o arsenal (dict)
            :param tropa: informações sobre a tropa (dict)
        """
        self.__arsenal = arsenal
        self.__tropa = tropa

    @property
    def arsenal(self):
        return self.__arsenal

    @arsenal.setter
    def arsenal(self, arsenal):
        self.__arsenal = arsenal

    @property
    def tropa(self):
        return self.__tropa

    @tropa.setter
    def tropa(self, tropa):
        self.__tropa = tropa
        
##############################################################
class SetorPrivado():
    """
        Classe que comporta informações sobre o setor privado de um país
    """
    def __init__(self, exportacao, importacao):
        """
            :param exportacao: lista de países para quem o país exporta (list(Pais))
            :param importacao: lista de países para quem o país importa (list(Pais))
        """
        self.__exportacao = exportacao # Lista de Países
        self.__importacao = importacao # Lista de Países   

    
    @property
    def exportacao(self):
        return self.__exportacao

    @exportacao.setter
    def exportacao(self, exportacao):
        self.__exportacao = exportacao
    
    @property
    def importacao(self):
        return self.__importacao

    @importacao.setter
    def importacao(self, importacao):
        self.__importacao = importacao
    
##############################################################
class Lider():
    """
        Classe que representa um líder
    """
    def __init__(self, nome, orientacao):
        """
            :param nome: nome do líder (str)
            :param orientacao: um numero inteiro [0 ou 1] representando a orientacao (int)
        """
        self.__nome = nome
        self.__orientacao = orientacao   
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def orientacao(self):
        return self.__orientacao

    @orientacao.setter
    def orientacao(self, orientacao):
        self.__orientacao = orientacao
    

##############################################################
class Acao():
    """
        Classe que representa genericamente um ação
    """
    def __init__(self, nome, ator, nomePanorama):
        """
            :param nome: nome da ação (str)
            :param ator: país ator da ação (Pais)
            :param nomePanorama: nome do panorama a ser afetado (str)
        """
        self.__nome = nome
        self.__ator = ator # Pais()
        self.__nomePanorama = nomePanorama
        # print(f'Criei acao {self.nome}!')
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def ator(self):
        return self.__ator

    @ator.setter
    def ator(self, ator):
        self.__ator = ator
        
    @property
    def nomePanorama(self):
        return self.__nomePanorama

    @nomePanorama.setter
    def nomePanorama(self, nomePanorama):
        self.__nomePanorama = nomePanorama
    

    def fazerEfeito(self, alvo, fator):
        """
            Acessar o panorama correto do ator e aplicar o fator na relação com o alvo
            :param alvo: país alvo da ação (Pais)
            :param fator: fator que irá acrescentar ou subtrair na relação (float)
        """
        # print(f'Entre fazerEfeitoi')
        # print(f'meu ator: {self.ator}')
        # print(f'meu alvo: {alvo}')

        if self.ator == alvo:
            raise Exception('Não inventa filho. Ação em si msm? WTF')

        # print(self.ator.setorEconomico)
        # self.ator.setorEconomico.aReceber[alvo.nome] = fator
        # alvo.setorEconomico.aPagar[self.ator.nome] = fator

        self.ator.mundo.panorama.alterarRelacao(self.ator, alvo, self.nomePanorama, fator)      

##############################################################
class InteracaoFixa():
    """
        Classe que representa o esqueleto das interações fixas
    """
    def __init__(self, membros, inicio, vigencia, fator):
        """
            :param membros: membros da interações (list(Pais))
            :param inicio: turno de inicio (int)
            :param vigencia: quantos turnos irá durar (int)
            :param fator: fator a ser aplicado na relação (float)
        """
        self.__membros = membros
        self.__inicio = inicio
        self.__vigencia = vigencia
        self.__fator = fator

        random_member = membros[[p for p in membros.keys()][0]]

        self.__mundo = random_member.mundo
    
    
    @property
    def membros(self):
        return self.__membros

    @membros.setter
    def membros(self, membros):
        self.__membros = membros
        
    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio
        
    @property
    def vigencia(self):
        return self.__vigencia

    @vigencia.setter
    def vigencia(self, vigencia):
        self.__vigencia = vigencia
        
    @property
    def fator(self):
        return self.__fator

    @fator.setter
    def fator(self, fator):
        self.__fator = fator
        
    @property
    def mundo(self):
        return self.__mundo

    @mundo.setter
    def mundo(self, mundo):
        self.__mundo = mundo
        
    def fazerEfeito(self):
        """
            método a ser sobreescrito nas interações
        """
        pass
    
##############################################################
class InteracaoMilitar(InteracaoFixa):
    """
        Classe que herda os atributos de InteraçãoFixa para representar uma interação militar
    """
    def __init__(self, membros, inicio, vigencia, fator):
        """
            atributos herdados de InteracaoFixa
            :param desfazer: identifica se a interação vai ser revertida ou não
        """
        super().__init__(membros, inicio, vigencia, fator)
        
    def fazerEfeito(self, desfazer = False):
        """
            MÉTODO SOBREESCRITO
            altera as relações entre os membros no panorama militar
        """

        # print(f"TIPO : {type(self.membros)}")

        panorama = 'militar'
        for membro in self.membros.values():
            for membro2 in self.membros.values():
                if membro == membro2:
                    if desfazer == True:
                        self.fator = (self.fator * -1)
                    continue
                self.mundo.panorama.alterarRelacao(membro, membro2, panorama, self.fator)

##############################################################
class InteracaoEconomica(InteracaoFixa):
    """
        Classe que herda os atributos de InteraçãoFixa para representar uma interação economica
    """
    def __init__(self, membros, inicio, vigencia, fator):
        """
            atributos herdados de InteracaoFixa
        """
        super().__init__(membros, inicio, vigencia, fator)
        
    def fazerEfeito(self, desfazer = False):
        """
            MÉTODO SOBREESCRITO
            altera as relações entre os membros no panorama economico
        """

        # print(f"TIPO : {type(self.membros)}")

        panorama = 'economico'
        for membro in self.membros.values():
            for membro2 in self.membros.values():
                if membro == membro2:
                    if desfazer == True:
                        self.fator = (self.fator * -1)
                    continue
                self.mundo.panorama.alterarRelacao(membro, membro2, panorama, self.fator)

##############################################################
class InteracaoPrivada(InteracaoFixa):
    """
        Classe que herda os atributos de InteraçãoFixa para representar uma interação privada
    """
    def __init__(self, membros, inicio, vigencia, fator):
        """
            atributos herdados de InteracaoFixa
        """
        super().__init__(membros, inicio, vigencia, fator)
    
    def fazerEfeito(self, desfazer = False):
        """
            MÉTODO SOBREESCRITO
            altera as relações entre os membros no panorama privado
        """

        # print(f"TIPO : {type(self.membros)}")

        panorama = 'privado'
        for membro in self.membros.values():
            for membro2 in self.membros.values():
                if membro == membro2:
                    if desfazer == True:
                        self.fator = (self.fator * -1)
                    continue

                self.mundo.panorama.alterarRelacao(membro, membro2, panorama, self.fator)

##############################################################
