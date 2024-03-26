#Início das variáveis globais
lista_livro = []
id_global = 0
#Função cadastrar_livro(id)
def cadastrar_livro(id):
  print('Qual livro gostaria cadastrar hoje?')
  print('Código do livro: {}'.format(id))
  nome = input('Digite o NOME do livro: ')
  autor = input('Digite o AUTOR do livro: ')
  editora = input('Digite a EDITORA do livro: ')
  dicionario = {'codigo'   : id,
                'nome'     : nome,
                'autor'    : autor,
                'editora'  : editora}
  lista_livro.append(dicionario.copy())
#Função consultar_livro()
def consultar_livro():
  print('Qual livro gostaria consultar hoje?')
  while True:
    consultar = input('\nEscolha a opção de consulta:\n'+
                      '1- Consultar TODOS\n'+
                      '2- Consultar por ID\n'+
                      '3- Consultar por AUTOR\n'+
                      '4- Retornar ao MENU ')
    if consultar == '1':
      print('Você escolheu consultar TODOS os livros')
      for livro in lista_livro:
        print('--------------------------')
        for key, value in livro.items():
          print('{}: {}'.format(key, value))
        print('--------------------------')
    elif consultar == '2':
      print('Você escolheu consultar por ID')
      valor_desejado = int(input('Digite o CÓDIGO desejado: '))
      for livro in lista_livro:
        if livro['codigo'] == valor_desejado:
          print('--------------------------')
          for key, value in livro.items():
            print('{}: {}'.format(key, value))
            print('--------------------------')
    elif consultar == '3':
      print('Você escolheu consultar por AUTOR')
      valor_desejado = input('Digite o AUTOR desejado: ')
      for livro in lista_livro:
        if livro['autor'] == valor_desejado:
          print('--------------------------')
          for key, value in livro.items():
            print('{}: {}'.format(key, value))
            print('--------------------------')
    elif consultar == '4':
      return
    else:
      print('Opção inválida. Tente novamente!')
      continue
#Função remover_livro()
def remover_livro():
  print('Qual livro gostaria de remover hoje?')
  valor_desejado = int(input('Digite o CÓDIGO que deseja remover: '))
  for livro in lista_livro:
    if  livro['codigo'] == valor_desejado:
      lista_livro.remove(livro)
      print('Livro removido com sucesso!')
#Início do laço principal
print('Bem-vindo(a) a Prateleira Virtual - Alessandra de Souza Oliveira')
while True:
  principal = input('\nEscolha a opção desejada:\n'+
                    '1- Cadastrar livro\n'+
                    '2- Consultar livro\n'+
                    '3- Remover livro\n'+
                    '4- sair\n'+
                    '>> ')
  if principal == '1':
    id_global = id_global + 1
    cadastrar_livro(id_global)
  elif principal ==  '2':
    consultar_livro()
  elif principal == '3':
    remover_livro()
  elif principal == '4':
    break
  else:
    print('Opção inválida, tente novamente!')
    continue