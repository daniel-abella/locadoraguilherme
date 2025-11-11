# 🎬 Gerenciador de Filmes em Python

Este projeto é um **mini-sistema de gerenciamento de filmes** feito em Python.  
Ele permite adicionar, listar, pesquisar, substituir e remover filmes de uma lista em memória.  
O objetivo é praticar **funções, listas e manipulação de dados via entrada do usuário.**

---

## 🧠 Conceito Principal

O programa trabalha com uma lista chamada `filmes`, que armazena os nomes dos filmes.  
Cada função realiza uma operação específica sobre essa lista.

---

## ⚙️ Funções do Programa

### 1. `obterQuantidadeFilmes(filmes)`
Exibe quantos filmes estão cadastrados atualmente.
```python
def obterQuantidadeFilmes(filmes):
    print("Atualmente temos", len(filmes), "filme(s).")
```
**Explicação:**  
Usa a função `len()` para contar os elementos da lista `filmes`.

---

### 2. `adicionarFilme(filmes)`
Adiciona um novo filme à lista.
```python
def adicionarFilme(filmes):
    novoFilme = input("Digite o nome do Filme: ")
    filmes.append(novoFilme)
    print("Filme adicionado com sucesso!")
```
**Explicação:**  
- Recebe o nome do novo filme via `input()`.  
- Adiciona o nome ao final da lista com `append()`.

---

### 3. `listarFilmes(filmes)`
Mostra todos os filmes cadastrados.
```python
def listarFilmes(filmes):
    if len(filmes) == 0:
        print("Nenhum filme foi encontrado.")
    else:
        print("Lista de Filmes")
        for filme in filmes:
            print("-", filme)
```
**Explicação:**  
- Verifica se a lista está vazia.  
- Se houver filmes, exibe um por linha usando um `for`.

---

### 4. `pesquisarFilme(filmes)`
Permite pesquisar um filme por sua posição.
```python
def pesquisarFilme(filmes):
    posicao = int(input("Digite a posição do filme: "))

    if posicao > 0 and posicao <= len(filmes):
        filmePesquisado = filmes[posicao - 1]
        print("O filme pesquisado foi", filmePesquisado)
    else:
        print("Nenhum filme foi encontrado para o código informado.")
```
**Explicação:**  
- O usuário informa a **posição** do filme (1, 2, 3...).  
- O código converte essa posição para o **índice da lista** (`posicao - 1`).  
- Exibe o nome correspondente ou uma mensagem de erro se o índice for inválido.

---

### 5. `substituirFilme(filmes)`
Substitui um filme existente por outro nome.
```python
def substituirFilme(filmes):
    posicao = int(input("Digite a posição do filme a ser substituído: "))

    if posicao > 0 and posicao <= len(filmes):
        novoNomeFilme = input("Digite o nome do filme: ")
        filmes[posicao - 1] = novoNomeFilme
        print("Filme substituído com sucesso!")
    else:
        print("Nenhum filme foi encontrado para o código informado.")
```
**Explicação:**  
- Solicita a posição do filme que será trocado.  
- Pede o novo nome e substitui diretamente o item na lista.

---

### 6. `removerFilme(filmes)`
Remove um filme da lista com base em sua posição.
```python
def removerFilme(filmes):
    posicao = int(input("Digite a posição do filme a ser removido: "))

    if posicao > 0 and posicao <= len(filmes):
        filmes.pop(posicao - 1)
        print("O filme foi removido")
    else:
        print("Nenhum filme foi encontrado para o código informado.")
```
**Explicação:**  
- Usa `pop()` para remover o filme pelo índice informado.  
- Valida se a posição existe antes de tentar remover.

---

## 🧪 Exemplo de Uso

```python
filmes = []

adicionarFilme(filmes)
adicionarFilme(filmes)
listarFilmes(filmes)
obterQuantidadeFilmes(filmes)
pesquisarFilme(filmes)
substituirFilme(filmes)
removerFilme(filmes)
listarFilmes(filmes)
```

---

## 🧰 Tecnologias Utilizadas

- 🐍 **Python 3**
- 💬 Funções e listas
- 🎯 Entrada e saída de dados (`input`, `print`)

---

## 💡 Possíveis Melhorias

- Criar um **menu interativo** com opções numéricas.  
- Salvar os filmes em um arquivo `.txt` ou `.json`.  
- Adicionar **validação de entrada** para evitar erros com letras em campos numéricos.
