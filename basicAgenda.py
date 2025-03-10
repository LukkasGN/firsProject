"""
Created on Fri Jul 23 10:01:05 2021

Finished on Wed Jul 28 16:00:03 2021

Author: Lucas Gabriel Nordio
"""

#Primeiro Projeto - agenda de contatos, com nome, telefone, e data de aniversário

"Variáveis"

nome_arquivo = 'primeiro_projeto.txt' #Criação de documeto caso não exista
dados = {}  #Nos dados vão entrar o nome:telefone/data de aniversário
strdados = 'str' #Transforma os dados de criação de contato em string sem caracteres adicionais
insnome = 'str' # No insnome, insdado e instel são apenas para criar o contato
instel = 'str' 
insniver = 'str'
seleção = 0 # Seleção de utilidades
selecnomeapagar = 'str' # Seleção de nome para apagar contato
linhas = 0 # Contagem de linhas
nomespesq = 'str' # Nomes pesquisados
result = [] # Lista de nomes pesquisados
pesquisa = 'str' #Nome a ser pesquisado em contatos
menu = True #Tratamento de colocação de dados no menu
numeros_foramenu = [6, 7, 8, 9, 0] #Remoção de numeros não utilizados no menu
numeros_para_nome = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] #Remoção de numeros para criação do nome no contato
passou = 0 #Variável if em casos de loop
passou2 = 0 #Variável if em casos de loop
passou3 = 0 #Variável if em casos de loop

"Programação"

#painel de seleção = 

while menu == True:
    try:
        seleção = int(input("Insira 1 para adicionar um contato, 2 para excluir um contato, 3 para pesquisar pelo nome, 4 para listar os contatos e 5 para sair: "))
    except ValueError:
        print("Deve ser um número ")
    if seleção in numeros_foramenu: #Seleção de operações
        print("O número deve ser entre 1 e 5!")
    else:
        break
    
#Inserir um contato =
    
if seleção == 1:
    with open(nome_arquivo, "a") as arquivo:
        while passou == 0:
            insnome = input("Insira um nome: ") #Colocar nome
            if insnome in numeros_para_nome:
                print("Não pode ter número!")
            else:
                break
        while passou2 == 0:
            try:
                instel = int(input("Insira o telefone: ")) #Colocar telefone
            except ValueError:
                print("Não pode conter letras, tente novamente: ")
            else:
                break
        insniver = input("Insira o aniversário: ") #Colocar aniversário
        dados[instel] = insniver
        strdados = repr(dados).replace("{", "").replace("}", "").replace("'", "") #tirar caracteres adicionais
        arquivo.write("\n" + insnome + " - ")
        arquivo.write(strdados)
        print("Contato criado!")
        
#Excluir um contato =

if seleção == 2:
    with open(nome_arquivo, 'r+') as arquivo2:
        linhas = arquivo2.readlines()
        while passou == 0:
            selecnomeapagar = input("Insira um Nome para apagar: ") #Qual nome será apagado
            if selecnomeapagar in numeros_para_nome:
                print("Não pode ter números, tente de novo: ")
            else:
                break
    with open(nome_arquivo, 'w') as arquivo3:
        for linha in linhas:
            if linha != selecnomeapagar + "\n":
                arquivo3.write(linha) #Reescrever todos os contatos menos o que se deseja apagar

#Pesquisar pelo nome =

if seleção == 3: 
    with open(nome_arquivo, 'r+') as arquivo4:
        pesquisa = input("Insira o nome de pesquisa:") #Colocação de nome a ser pesquisado
        nomespesq = arquivo4.readlines() #Separar em linhas
        for nome in nomespesq:
            if pesquisa.lower() in nome.lower() + "\n":
                nome = nome.replace('\n', ' ')
                result.append(nome) #Adicionar nome encontrado à lista
        result2 = str(result) #Transformar lista em string
        result3 = result2.replace("[", "").replace("]", "").replace(" "" ", "").replace("{", "").replace("}", "") #Tirar caracteres indesejados da string
        if len(result) >= 1:
            print(result3)
        if len(result) < 1 : #Verificação em caso de não haver contatos com o nome
            print("Sem contatos com esse nome. ")

#Listar =

if seleção == 4:
    with open(nome_arquivo, 'r') as arquivo2:
        apresentação = str(arquivo2.read()) #Transofrmar arquivo em string
        if apresentação == '':
            print("O arquivo está vazio! ")
        else:
            apresentação2 = apresentação.replace("[", "").replace("]", "").replace(" "" ", "").replace("{", "").replace("}", "") #Tirar caracteres indesejados da lista
            print(apresentação2)

#Sair =

if seleção == 5:
    print("Programa fechado!")
