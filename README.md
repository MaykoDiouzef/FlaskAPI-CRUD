# FlaskAPI
# 1 - Introdução ao Flask

Lançado em 2010 e desenvolvido por Armin Ronacher, o Flask é um micro-framework destinado principalmente a pequenas aplicações com requisitos mais simples, como por exemplo, a criação de um site básico.

![Armin Ronacher](imagens\1200px-Armin_Ronacher_in_August_2014.jpg)

Possui um núcleo simples e expansível que permite que um projeto possua apenas os recursos necessários para sua execução (conforme surja a necessidade, um novo pacote pode ser adicionado para incrementar as funcionalidades da aplicação).

## 1.1 - Características do Flask

### 1.1.1 - Simplicidade
Por possuir apenas o necessário para o desenvolvimento de uma aplicação, um projeto escrito com Flask é mais simples se comparado aos frameworks maiores, já que a quantidade de arquivos é muito menor e sua arquitetura é muito mais simples.

### 1.1.2 - Rapidez no Desenvolvimento
Com o Flask, o desenvolvedor se preocupa em apenas desenvolver o necessário para um projeto, sem a necessidade de realizar configurações que muitas vezes não são utilizadas.

### 1.1.3 - Projetos Menores
Por possuir uma arquitetura muito simples (um único arquivo inicial) os projetos escritos em Flask tendem a ser menores e mais leves se comparados a frameworks maiores.

### 1.1.4 - Aplicações Robustes
Apesar de ser um micro-framework, o Flask permite a criação de aplicações robustas, já que é totalmente personalizável, permitindo, caso necessário, a criação de uma arquitetura mais definida.

## 1.2 - Pré-requisitos

Antes de começar, você vai precisar ter o seguinte instalado em sua máquina:

- [Python 3.6+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)

## 2 - Preparação do Ambiente

Primeiro, crie uma pasta chamada "Flask" na área de trabalho e abra o terminal dentro dessa pasta.

## 3 - Instalação do PIP

Pip é um sistema de gerenciamento de pacotes padrão, usado para instalar e gerenciar pacotes de software escritos em Python.

Abrir o terminal, pode ser em qualquer diretório e digitar/colar o seguite comando:

      sudo apt install python3-pip

## 4 - Configuração do Ambiente Virtual

Um ambiente virtual é uma instância independente do Python, que permite isolar as bibliotecas e dependências de um projeto específico. Isso é útil para evitar conflitos entre diferentes versões de pacotes e garantir que o projeto seja executado consistentemente, independentemente do ambiente de desenvolvimento.

### 4.1 - Instalando a biblioteca venv

O *venv* é uma biblioteca Python padrão, capaz de criar ambiente virtual, disponível nas versões 3.3 e posteriores.

Para instalar a biblioteca venv no Windows, Linux ou Mac, abra o terminal use o seguinte comando:

      sudo apt install python3-venv

### 4.2 - Criando o Ambiente Virtual

Dentro do diretório do seu projeto, onde está localizado o arquivo main.py, *sendo este o diretório raiz do projeto*, crie um ambiente virtual:  
*Observação: O **nome** do ambiente virtual pode ser de seu escolha, neste projeto o nome será **ambiente-virtual***

      python3 -m venv ambiente-virtual

### 4.3 - Ativando o Ambiente Virtual

#### 4.3.1 - Windows

Para ativar o ambiente virtual no Windows, use um dos seguintes comandos, dependendo do seu terminal:  
*Observação: O **Visual Studio Code** no **Windows** usa o **Terminal PowerShell***

Terminal normal

      .\ambiente-virtual\Scripts\activate.bat

Terminal PowerShell

      .\ambiente-virtual\Scripts\Activate.ps1

#### 4.3.2 - Linux e Mac

Para ativar o ambiente virtual no Linux ou Mac, use o seguinte comando:

      source ambiente-virtual/bin/activate

#### 4.3.3 - Ambiente virtual ativo

Como deve ficar se o ambiente virtual estiver ativo:

![Ativo no Windows - Normal](imagens\normal.png)
![Ativo no Linux](imagens\linux.png)


### 4.4 - Desativando o Ambiente Virtual
Para desativar o ambiente virtual no Windows, Linux ou Mac, use:

      deactivate

# 5 - Instalando bibliotecas

Dentro do arquivo *requirements.txt* deve conter todas as bibliotecas que vamos utilizar dentro do projeto, para não ter a necessidade de instalar uma por uma manualmente. Vamos instalar todas juntas,  pedido para o pip instalar todas bibliotecas que foram listadas dentro do arquivo, necessario informar o nome e se quiser, a vesão da biblioteca.

## 5.1 - Lista de bibliotecas

Abrir o arquivos *requirements.txt* e digitar/colar a lista de bibliotecas utilizadas:

      Flask==3.0.3
      PyMySQL==1.1.1
      requests==2.32.3
      responses==0.25.3
      SQLAlchemy==2.0.31

## 5.2 - Comando de instalação

Para instalar as bibliotecas, é necessario abrir o terminal na pasta raiz que o *requirements.txt* está localizado e executar o seguinte comando:  
**Atenção: Este comando deve ser executado dentro do ambiente virtual, caso contrario, todas as bibliotecas serão instaladas na maquina.**

      pip install -r requirements.txt


# 6 - Ambiente Docker
      docker compose up --build -d


