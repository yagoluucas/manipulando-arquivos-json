"""
Considere que o arquivo “notas.CSV” apresenta uma listagem com os dados dos alunos de uma turma.
Cada linha do arquivo apresenta os dados de um aluno, no formato:
RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
Implemente um programa que leia esse arquivo CSV e a partir dele gere um novo arquivo JSON no formato:
{
    "2101254": {
        "nome": "Benicio Pires",
        "notas": [
            3.6,
            10.0,
            8.5,
            7.0
        ]
    },
    "2101624": {
        "nome": "Bruna Goncalves",
        "notas": [
            9.5,
            8.0,
            6.0,
            5.5
        ]
    }
}
"""
import json

with open('notas.csv', 'r', encoding='utf-8') as arquivo_csv:
    arquivo_csv.__next__()
    dicionario = {}
    for linha in arquivo_csv:
        lista = linha.split(',') # transforma a linha em um array
        notas = lista[2:] # pegando somente as notas
        notas[3] = notas[3].replace('\n', '') # tirando o \n do ultimo item
        info_aluno = {'nome': lista[1], 'notas': notas}
        dicionario[lista[0]] = info_aluno
    with open('arquivos/ex1.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)

