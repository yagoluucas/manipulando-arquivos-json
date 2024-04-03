"""
Implemente um sistema para cadastro de Pets, com as opções Inserir, Excluir, Listar Todos.
Utilize um arquivo JSON para armazenar as informações.
O arquivo JSON deve ter a estrutura abaixo e conforme as operações realizadas, o arquivo deve ser modificado

[
    {
        "tipo": "Cachorro",
        "nome": "Bebel",
        "idade": 4
    },
    {
        "tipo": "Hamster",
        "nome": "Pimpão",
        "idade": 2
    },
    {
        "tipo": "Cavalo",
        "nome": "Trovão",
        "idade": 6
    }
]
"""
import json


def cadastrar_pet():
    """ Função responsável por cadastrar pets """
    try:
        with open('arquivos/ex3.json', 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)  # transforma em um array
    except:
        print('Erro ao ler arquivo')
    try:
        with open('arquivos/ex3.json', 'w', encoding='utf-8') as arquivo:
            dicionario = {}
            dicionario['tipo'] = input("Digite o tipo do seu pet: ")
            dicionario['nome'] = input("Digite o nome do seu pet: ")
            dicionario['idade'] = int(input("Digite a idade do seu pet: "))
            lista.append(dicionario)  # adiciona o pet em um array
            json.dump(lista, arquivo, ensure_ascii=False, indent=4)
    except:
        print('Erro ao escrever no arquivo')


def excluir_pets(lista_pet: list):
    """ Função responsável por excluir pets """
    try:
        with open('arquivos/ex3.json', 'w', encoding='utf-8') as arquivo:
            while True:
                nome_pet = input('Digite o nome do pet que você deseja excluir ou zero para sair: ')
                if len(lista_pet) <= 0 or nome_pet == '0':
                    print('Saindo do menu' if nome_pet == '0' else 'Sem mais nenhum pet cadastrado')
                    break
                else:
                    for item in lista_pet:
                        if item['nome'].lower() == nome_pet.lower():
                            lista_pet.remove(item)
                            print('Pet removido')
            json.dump(lista_pet, arquivo, ensure_ascii=False, indent=4)

    except:
        print('Erro ao excluir pet')


while True:
    lista_pet = []
    try:
        arquivo = open('arquivos/ex3.json', 'r', encoding='utf-8')
        lista_pet = json.load(arquivo)
        arquivo.close()
    except:
        with open('arquivos/ex3.json', 'w') as arquivo:
            json.dump([], arquivo)
        print('O arquivo nao existia ou estava inconsistente, '
              'criamos um novo no diretório arquivos com o nome ex3!')
        print('O programa será encerrado para poder atualizar, '
              'peço que rode novamente para poder fazer sua solicitação')
        break
    print("-- Bem vindo ao sistema de pets --")
    match input("Escolha uma opção: \n"
                "1 - Cadastrar Pets\n"
                "2 - Excluir Pets\n"
                "3 - Listar Todos\n"
                "0 - Sair\n"):
        case '1':
            cadastrar_pet()
        case '2':
            if len(lista_pet) >= 1:
                excluir_pets(lista_pet)
            else:
                print('Sem nenhum pet cadastrado')
        case '3':
            if len(lista_pet) >= 1:
                for item in lista_pet:
                    print(item)
            else:
                print('Nenhum pet cadastrado')
        case '0':
            break
        case _:
            print('Opção incorreta, voltando ao menu')
