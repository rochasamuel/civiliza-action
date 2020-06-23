##############################################################
class Mundo():
    """
        Classe onde todos os outros objetos vão residir. Vai ser usada majoritariamente como um hub de informações.
    """
    def __init__(self):
        """
            A classe é instanciada sem nenhum atributo porque eles são instaciados depois, recebendo Mundo() como attr.
        """
        self.paises = {} # é um dicionário no formato {'nome_pais':Pais()}
        self.ano = 1 # Variável de contagem de turnos
        self.interacoesFixas = [] # Lista com os objetos interacaoFixa()
        self.panorama = None # Panorama() do mundo, com os três filhos

    def testebranch():
        pass
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
            nomesAleatorios.add(random.choice(self.paises.keys()))

        nomesAleatorios = sorted(list(nomesAleatorios))

        nomesAleatorios = {pais: self.paises[pais] for pais in nomesAleatorios}

        return nomesAleatorios
        
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

        # Teste para não ter países: raise alguma coisa
        if len(mundo.paises) == 0:
            # Exceção aqui
            pass

        listaDePaises = mundo.paises.keys()
        n_paises = len(listaDePaises)

        self.economico = pd.DataFrame(np.random.rand(n_paises, n_paises), index=listaDePaises, columns=listaDePaises)
        self.privado = pd.DataFrame(np.random.rand(n_paises, n_paises), index=listaDePaises, columns=listaDePaises)
        self.militar = pd.DataFrame(np.random.rand(n_paises, n_paises), index=listaDePaises, columns=listaDePaises)

        self.geral = self.economico + self.privado + self.militar

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
            self.militar.loc[A, B] += fator
            self.militar.loc[B, A] += fator

            self.atualizarPanorama()

        if nomePanorama == 'privado':
            self.privado.loc[A, B] += fator
            self.privado.loc[B, A] += fator

            self.atualizarPanorama()

        if nomePanorama == 'economico':
            self.economico.loc[A, B] += fator
            self.economico.loc[B, A] += fator

            self.atualizarPanorama()

##############################################################
class Pais():
    """
        Classe que representa um país. Será atribuido a um jogador
    """
    def __init__(self, nome, populacao, 
    imigrantes, continente, 
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
        self.nome = nome
        self.continente = continente
        self.setorEconomico = setorEconomico
        self.setorMilitar = setorMilitar
        self.setorPrivado = setorPrivado
        self.lider = lider
        self.mundo = mundo

        self.mundo.paises[self.nome] = self #se adiciona na lista de países do mundo
        
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
        self.limite_aReceber = limite_aReceber
        self.limite_aPagar = limite_aPagar
        
        self.aPagar = pd.Series(dtype = float)
        self.aReceber = pd.Series(dtype = float)
        
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
        self.arsenal = arsenal
        self.tropa = tropa
        
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
        self.exportacao = exportacao # Lista de Países
        self.importacao = importacao # Lista de Países   
    
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
        self.nome = nome
        self.orientacao = orientacao   

##############################################################
class Acao():
   pass

    def fazerEfeito(self):
        pass        

##############################################################
class InteracaoFixa():
    pass

    def fazerEfeito(self):
        pass
    
##############################################################
class InteracaoMilitar(InteracaoFixa):
    pass
        
    def fazerEfeito(self):
        pass        

##############################################################
class InteracaoEconomica(InteracaoFixa):
    pass

    def fazerEfeito(self):
        pass

##############################################################
class InteracaoPrivada(InteracaoFixa):
    pass

    def fazerEfeito(self):
        pass

##############################################################
class Jogador(Pais):
    pass