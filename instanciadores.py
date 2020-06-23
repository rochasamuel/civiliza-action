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
    """
    return setorEconomico(
        np.random.randint(50,100),
        np.random.randint(10),
        np.random.randint(10), 
        0)

def createSetorMilitar():
    pass

def createSetorPrivado():
    pass

def createLider():
    pass

def createPais(nome, mundo):
    pass
   
def createInteracaoFixa(mundo):
    pass