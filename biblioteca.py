# Lib para alinhamento de livros e registro de novos livros

# - >  Requisitos funcionais
# 1) Armazenar livros
# 2) Permitir que o usuário consiga cadastrar mais livros
# 3) Buscar um livro específico através do ISBN

# - > Não funcional
# I) A lib deve ter função que liste todos os livros em ordem alfabética via título
# II) A lib deve ter função que possa listar os livros via gênero

#-----------------------------------------------------------------------------


# add_livro recebe 1 argumento (variável Global) de livros type = dict e adiciona 
# um novo livro. A chave é o IBSM do livro, o valor da chave é um type = tuple 
# com as informações do livro: Titulo, autoria, genero
def add_livro(newbook): 
    print("""
    ADICIONANDO NOVO LIVRO:
    Forneça as seguintes informações do novo livro:
    """)
    isbm = input('ISBM ')
    (x,y,z) = (input('Nome do livro '),input('Autoria '),input('Qual gênero pertence? '))
    newbook[int(isbm)] = (x,y,z)
    
# procurar_book recebe 2 argumentos (identificação IBSM e variável Global) e procura 
# o livro pela chave IBSM   
def procurar_book(ibsm, lib):
    return lib.get(ibsm,'ERROR 404') 


# alinhar_genero recebe 1 argumento (variável global)
# Gera uma lista ordenada de acordo com o genero dos livros.
# Funcao sorted percorre os tuples, cata o genero que ta no slot 2
# pega a string e transforma em letras minúculas e alinha ascendente
def alinhar_genero(lib):
    lista_auxiliar = sorted(lib.values(), key = lambda x: x[2].lower())
    return lista_auxiliar


# alinhar_titulo recebe 1 argumento (variável global)
# Gera uma lista ordenada de acordo com o título dos livros.
# Funcao sorted percorre os tuples, cata o titulo que ta no slot 0
# pega a string e transforma em letras minúculas e alinha ascendente
def alinhar_titulo(lib):
    lista_auxiliar = sorted(lib.values(), key = lambda x: x[0].lower())
    return lista_auxiliar