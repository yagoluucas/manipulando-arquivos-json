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


def cadastrar_pet(lista_pet: list):
    """ Função responsável por cadastrar pets """
    try:
        with open('arquivos/ex3.json', 'w', encoding='utf-8') as arquivo:
            dicionario = {}
            dicionario['tipo'] = input("Digite o tipo do seu pet: ")
            dicionario['nome'] = input("Digite o nome do seu pet: ")
            dicionario['idade'] = int(input("Digite a idade do seu pet: "))
            lista_pet.append(dicionario)  # adiciona o pet em um array
            json.dump(lista_pet, arquivo, ensure_ascii=False, indent=4)
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

def atualizar_pets(lista_pet: list):
    """ Função resposável por atualizar os pets cadastrados """
    try:
        with open('arquivos/ex3.json', 'w', encoding='utf-8') as arquivo:
            pet_encontrado = False
            nome_pet = input('Digite o nome do pet que você deseja atualizar: ')
            for item in lista_pet:
                if item['nome'] == nome_pet:
                    item['tipo'] = input('Digite o novo tipo do pet: ')
                    item['nome'] = input('Digite o novo nome do pet: ')
                    item['idade'] = int(input('Digite a nova idade do pet: '))
                    print('Pet atualizado com sucesso')
                    pet_encontrado = True
            if not pet_encontrado:
                print('Pet não encontrado')
            else:
                json.dump(lista_pet, arquivo, ensure_ascii=False, indent=4)
    except:
        print('Erro ao atualizar pet')

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
                "4 - Atualizar Pets\n"
                "0 - Sair\n"):
        case '1':
            cadastrar_pet(lista_pet)
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
        case '4':
            if len(lista_pet) >= 1:
                atualizar_pets(lista_pet)
            else:
                print('Sem nenhum pet cadastrado')
        case '0':
            break
        case _:
            print('Opção incorreta, voltando ao menu')
