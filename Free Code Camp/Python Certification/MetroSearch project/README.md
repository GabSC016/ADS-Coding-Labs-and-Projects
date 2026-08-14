# 🚇 Metro Search App

> Sistema de consulta de uma rede de metrô desenvolvido em Python, utilizando Programação Orientada a Objetos e o algoritmo BFS para encontrar o melhor trajeto entre estações.

---

## 📌 Sobre o projeto

O **Metro Search App** é uma aplicação de terminal que simula uma pequena rede de metrô.

O sistema permite consultar:

* 🚇 Linhas do metrô
* 📍 Estações
* 🔗 Conexões entre estações
* 🚉 Linhas associadas a uma estação
* 🔄 Conexões diretas entre estações
* 🧭 Melhor trajeto entre duas estações

O projeto foi desenvolvido como uma forma prática de aplicar conceitos de **Python, Programação Orientada a Objetos, estruturas de dados e algoritmos de busca**.

---

## ✨ Funcionalidades

| Opção | Funcionalidade                      |
| :---: | ----------------------------------- |
|  `1`  | 🚇 Consultar linhas                 |
|  `2`  | 📍 Consultar estações               |
|  `3`  | 🔗 Consultar conexões               |
|  `4`  | 🚉 Consultar linhas de uma estação  |
|  `5`  | 🔄 Verificar conexão entre estações |
|  `6`  | 🧭 Encontrar melhor trajeto         |
|  `0`  | 🚪 Sair                             |

---

# 🗺️ Mapa da rede

A aplicação utiliza uma rede composta por **15 estações**, identificadas de `A` até `O`.

```text
A - B - C - D - E
        │
F - G - C - H - I
            │
J - K - H - L - M
    │       │
N - O - D - J - L
```

### Linhas

```text
🔴 Red Line
A → B → C → D → E

🔵 Blue Line
F → G → C → H → I

🟢 Green Line
J → K → H → L → M

🟡 Yellow Line
N → O → D → J → L
```

### 🔄 Estações de transferência

Algumas estações pertencem a mais de uma linha:

| Estação | Linhas                         |
| :-----: | ------------------------------ |
|   `C`   | 🔴 Red Line + 🔵 Blue Line     |
|   `D`   | 🔴 Red Line + 🟡 Yellow Line   |
|   `H`   | 🔵 Blue Line + 🟢 Green Line   |
|   `J`   | 🟢 Green Line + 🟡 Yellow Line |
|   `L`   | 🟢 Green Line + 🟡 Yellow Line |

---

# 🖥️ Demonstração

## 🚇 Menu principal

Ao iniciar o programa, o usuário encontra o menu principal:

```text
==================================================
                 METRO SEARCH APP
==================================================

        Olá, seja bem-vindo ao Metro Search.

             Escolha uma opção abaixo:
--------------------------------------------------
|1| Consultar linhas
|2| Consultar estações
|3| Consultar conexões
|4| Consultar linhas de uma estação
|5| Verificar conexão entre estações
|6| Encontrar melhor trajeto
|0| Sair
--------------------------------------------------
```

---

## 🚇 Consultar uma linha

Ao selecionar a opção `1`, o usuário escolhe uma das linhas disponíveis.

Exemplo:

```text
Digite uma opção válida: 1

Digite uma opção válida: 1
```

Resultado:

```text
==================================================
                  Estações da Red Line
==================================================
                A --> B --> C --> D --> E
==================================================
```

---

## 🔗 Consultar conexões

A opção `3` permite consultar as conexões de uma estação.

Exemplo:

```text
Digite uma opção válida: 3

Digite uma opção válida: C
```

Resultado:

```text
==================================================
               CONEXÕES DA ESTAÇÃO C
==================================================
             Total de conexões: 4
          Conectada a: B • D • G • H
==================================================
```

---

## 🚉 Consultar linhas de uma estação

A opção `4` permite descobrir quais linhas passam por uma determinada estação.

Exemplo:

```text
Digite uma opção válida: 4

Digite uma opção válida: C
```

Resultado:

```text
==================================================
               LINHAS DA ESTAÇÃO C
==================================================
               Linhas: Red Line • Blue Line
             Estação de transferência
==================================================
```

---

## 🔄 Verificar conexão direta

A opção `5` verifica se duas estações possuem uma **conexão direta**.

Exemplo:

```text
Digite uma estação: C
Digite outra estação para verificar a conexão: G
```

Resultado:

```text
==================================================
             CONEXÃO ENTRE ESTAÇÕES
==================================================
                    ✓ C ↔ G
          As estações estão diretamente conectadas.
==================================================
```

Caso não exista uma conexão direta:

```text
==================================================
             CONEXÃO ENTRE ESTAÇÕES
==================================================
                    ✗ C ↛ E
       As estações não estão diretamente conectadas.
==================================================
```

> **Observação:** essa funcionalidade verifica apenas uma conexão direta. Ela não procura um caminho alternativo.

---

# 🧭 Encontrando o melhor trajeto

Uma das principais funcionalidades do projeto é encontrar o menor caminho entre duas estações.

Para isso, o sistema utiliza o algoritmo:

## BFS — Breadth-First Search

A rede de metrô pode ser representada como um **grafo**, onde:

* cada estação representa um **vértice**;
* cada conexão representa uma **aresta**.

Por exemplo:

```text
==================================================
             MELHOR CAMINHO ENCONTRADO
==================================================
Origem : A
Destino: M
Rota   : A --> B --> C --> H --> L --> M
Paradas: 5
==================================================
```

Como todas as conexões possuem o mesmo peso, o BFS encontra um caminho com o **menor número de conexões/paradas**.

---

# 🏗️ Arquitetura

O projeto utiliza diferentes classes para representar os elementos da aplicação:

```text
                 Metro
                   │
          ┌────────┴────────┐
          │                 │
        Line             Station
          │                 │
          │                 ├── connections
          │                 └── lines
          │
          └── stations

             InterfaceMetroApp
                     │
                     ├── menus
                     ├── validações
                     └── interação com usuário
```

---


Este projeto reúne diversos conceitos importantes de Python.

### 🐍 Python

* Variáveis
* Condicionais
* Loops
* Funções
* F-strings
* Listas
* Tuplas
* Sets
* Dicionários
* List comprehension
* Tratamento de exceções
* Validação de entradas

### 🏛️ Programação Orientada a Objetos

* Classes
* Objetos
* Atributos
* Métodos
* Herança
* `super()`
* `isinstance()`
* Composição entre objetos

### 🧠 Algoritmos e estruturas de dados

* Representação de grafos
* Busca em largura
* BFS — Breadth-First Search
* Reconstrução de caminhos
* Controle de elementos visitados

---