# FlaskAPI-CRUD
# Introdução ao Flask

Lançado em 2010 e desenvolvido por Armin Ronacher, o Flask é um micro-framework destinado principalmente a pequenas aplicações com requisitos mais simples, como por exemplo, a criação de um site básico.

![Armin Ronacher]((https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Armin_Ronacher_in_August_2014.jpg/330px-Armin_Ronacher_in_August_2014.jpg))

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

# apt install python3-venv

# python -m venv ambiente-virtual

# Windows
# Para ativar
.\ambiente-virtual\Scripts\activate.bat
.\ambiente-virtual\Scripts\Activate.ps1
# Para desativar
deactivate

# Linux e Mac
# Para ativar
source ambiente-virtual/bin/activate
# Para desativar
deactivate

# Comando
docker compose up --build -d

# Instalando bibliotecas
pip3 install requests
pip3 install SQLAlchemy
pip3 install PyMySQL

https://docs.sqlalchemy.org/en/20/core/engines.html
https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html
