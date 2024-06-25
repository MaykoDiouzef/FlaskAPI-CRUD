# FlaskAPI-CRUD
# Introdução ao Flask

Lançado em 2010 e desenvolvido por Armin Ronacher, o Flask é um micro-framework destinado principalmente a pequenas aplicações com requisitos mais simples, como por exemplo, a criação de um site básico.

![Armin Ronacher](https://www.palletsprojects.com/images/armin.jpg)

Possui um núcleo simples e expansível que permite que um projeto possua apenas os recursos necessários para sua execução (conforme surja a necessidade, um novo pacote pode ser adicionado para incrementar as funcionalidades da aplicação).

## Características do Flask

### Simplicidade
Por possuir apenas o necessário para o desenvolvimento de uma aplicação, um projeto escrito com Flask é mais simples se comparado aos frameworks maiores, já que a quantidade de arquivos é muito menor e sua arquitetura é muito mais simples.

### Rapidez no Desenvolvimento
Com o Flask, o desenvolvedor se preocupa em apenas desenvolver o necessário para um projeto, sem a necessidade de realizar configurações que muitas vezes não são utilizadas.

### Projetos Menores
Por possuir uma arquitetura muito simples (um único arquivo inicial) os projetos escritos em Flask tendem a ser menores e mais leves se comparados a frameworks maiores.

### Aplicações Robustes
Apesar de ser um micro-framework, o Flask permite a criação de aplicações robustas, já que é totalmente personalizável, permitindo, caso necessário, a criação de uma arquitetura mais definida.

## Pré-requisitos

Antes de começar, você vai precisar ter o seguinte instalado em sua máquina:

- [Python 3.6+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Preparação do Ambiente

Primeiro, crie uma pasta chamada "Flask" na área de trabalho e abra o terminal dentro dessa pasta.

## Instalação do PIP

      sudo apt install python3-pip

## Configuração do Ambiente Virtual

Para evitar conflitos entre dependências e manter seu projeto organizado, é recomendável utilizar um ambiente virtual.

### Instalando o módulo venv

Para instalar o módulo venv no Linux, use o seguinte comando:

      sudo apt install python3-venv

### Criando o Ambiente Virtual

Dentro do diretório do seu projeto, onde está localizado o arquivo main.py, crie um ambiente virtual:

      python -m venv ambiente-virtual

### Ativando o Ambiente Virtual

#### Windows

Para ativar o ambiente virtual no Windows, use um dos seguintes comandos, dependendo do seu terminal:

      .\ambiente-virtual\Scripts\activate.bat

Para desativar o ambiente virtual no Windows, use:

      deactivate

#### Linux e Mac

Para ativar o ambiente virtual no Linux ou Mac, use o seguinte comando:

      source ambiente-virtual/bin/activate

Para desativar o ambiente virtual no Linux ou Mac, use:

      deactivate

# Comando
      docker compose up --build -d

# Instalando bibliotecas
      pip install -r requirements.txt
