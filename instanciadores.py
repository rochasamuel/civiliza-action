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
    pass

def createPais(nome, mundo):
    pass
   
def createInteracaoFixa(mundo):
    pass