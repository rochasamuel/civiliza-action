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
    pass
        
##############################################################
class setorEconomico():
    pass
        
##############################################################
class setorMilitar():
    pass
        
##############################################################
class setorPrivado():
    pass    
    
##############################################################
class Lider():
    pass    

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