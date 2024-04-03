import json
"""
Considere o arquivo “foods.CSV”, com três colunas, no formato abaixo, onde cada linha representa um indivíduo
com suas respectivas informações.

NAME,ID,FAVORITE FOOD
Implemente um programa que a partir do arquivo indicado gere um arquivo JSON no formato abaixo:
{
    "1": {
    "nome": "John Doe",
    "food": "pizza"
    },
    "2": {
    "nome": "Jane Smith",
    "food": "sushi"
    },
    "3": {
    "nome": "Michael Johnson",
    "food": "steak"
    }
}
"""

with open('foods.csv', 'r', encoding='utf-8') as arquivo:
    arquivo.__next__() # pula a primeira linha
    dicionario = {}
    for linha in arquivo:
        lista = linha.split(',') # transforma a linha em um array
        dados_usuario = {}
        id = lista[1] # pega o id
        dados_usuario['nome'] = lista[0] # pega o nome e coloca no dicionário
        dados_usuario['food'] = lista[2].replace('\n', '') # pega a comida e coloca no dicionário
        dicionario[str(id)] = dados_usuario
    with open('arquivos/ex2.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)




