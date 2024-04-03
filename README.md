# Manipulação de arquivos JSON em Python

## Objetivo

Objetivo desse projeto é implementar um sistema em python que manipule arquivos em JSON em 3 exercicíos diferentes que
foram passados na minha matéria computational thinking using python

## Requisitos

Para poder rodar esse programa, é necessário ter os seguintes requisitos:
- Python na versão 3.11 ou superior
- Ter uma IDE da sua escolha, sendo recomendado o pycharm

## Sobre os exercicios

### Exercicio 1
Neste exercício foi solicitado manipular o arquivo csv chamado notas.csv e transformar ele em um arquivo json
seguindo os requisitos:

Considere que o arquivo `notas.CSV` contém uma lista com os dados dos alunos de uma turma. Cada linha do arquivo apresenta os dados de um aluno no formato: `RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4`.

A tarefa é implementar um programa que leia este arquivo CSV e gere um novo arquivo JSON no seguinte formato:

```json
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
```

## Exercicio 2
Neste exercicio foi solicitado para manipular o arquivo csv `foods.csv` e transformar ele em um arquivo json, seguindo os requisitos:

Considere o arquivo “foods.CSV”, com três colunas, no formato abaixo, onde cada linha representa um indivíduo 
com suas respectivas informações.
`NAME,ID,FAVORITE FOOD`   
Implemente um programa que a partir do arquivo indicado gere um arquivo JSON no formato abaixo:
```json
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
```

## Exercicio 3
Neste exercício foi solicitado para gerar um crud na qual o usuário pode adicionar, remover, atualizar e listar
os seus pets, colocando o nome, idade e o tipo de pet na qual o arquivo deverá ficar nessa estrutura  
```json
[
    {
        "tipo": "Gato",
        "nome": "Frajola",
        "idade": 3
    },
    {
        "tipo": "Cachorro",
        "nome": "Rex",
        "idade": 5
    }
]
```

## Resolução
Foram implementados 3 arquivos python para resolver cada um dos exercícios, sendo eles:
- `ex1.py`
- `ex2.py`
- `ex3.py`

Cada arquivo tem a sua respectiva resolução e foi feito testes para garantir que o programa está funcionando corretamente

## Conclusão
Com esse projeto, foi possível aprender a manipular arquivos JSON em python e como é feito a leitura e escrita desse tipo de arquivo

