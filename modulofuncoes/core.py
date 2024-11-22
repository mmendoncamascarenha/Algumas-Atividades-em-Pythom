def somalista(valores=[]):
    """
    A função somalista, recebe uma lista de números e faz a soma de todos os números da lista e retorna 
    o resultado da soma
     
    
    Parameters
    -----------------------------------------------------------
    valores: int[]
        lista de números para a soma


    Returns
    -----------------------------------------------------------
        retorna a soma de uma lista 
    """
    [1,2,34,56,687,51]

    resultado = 0 
    for i in valores:
        resultado+=i

    return resultado 

def maiorValor(lista=[]):
    """
    A função maiorValor encontra o maior valor em uma lista numérica

    Parameters
    ------------------------------------------------------------
        lista: int[]
    
    returns
    -------------------------------------------------------------
        retorna o maior valor da lista 
    """

    m = lista[0]
    for i in lista:
        if i > m:
            m = i
    
    return m 

def inverter(palavra=""):

    #vamos utilizar p comando len (length-comprimento) para obter a quantidade de caracteres da palavra 
    qtd = len(palavra)
    invertida = " "
    for i in range(qtd-1,-1,-1):
        invertida+=palavra[i]
    return invertida

def palindromo(palavra=" "):
    org = inverter(palavra).lower
    if palavra.lower()==org:
        return "é um palindromo"
    else:
        return"Não é um palindromo"
    
