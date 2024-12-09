# Changelog SupperSupply

## 20241209


## 20241208
Configuring Java and Intellij to work with maven

workstation (Ubuntu 22.04)
- install intellij community `$ sudo snap install intellij-idea-community --classic`
- install openjdk `$ sudo apt install openjdk-21-jdk`
- install maven `$ sudo apt install maven`

starting project:
access https://start.spring.io/ to generate project basis
I'm using chatgpt+gemini to help with it. Apparently java using spring + maven uses the folder structure as its namespaces/packages.
- the spring database lib/package has created the tables that was missing... bah. I want more control. But that is ok. Looks like the basic user service is up and running. It's time create its own database, and make it run as a container.


## 20241203 - SupperSupply has been started!
It's a fictional company that distributes suppers. With multiples warehouses, pick up and delivery points, a vehicle fleet moves suppers all around.
My idea is to use multiple languages to create an IT ecosystem that provides for all company's needs regarding managing suppers and their whereabouts. The goal is to showoff my technical skills and abilities in a more complex scenario.

Languages Goals: C#, Java, Python, Node, Javascript (and React), PHP?, maybe somethin in mobile?, maybe some Godot?
I will compile a definitive list of technologies and concepts in README file.
The final solution should require only git and docker to run, and a single `docker compose up` should be all that is needed.

for now let's start with the first service: User service. It will be done in Java and MySql.




---
_OLD_
# Changelog MStarSupply

## v0.1.0
- __ - **api** - adicionar test coverage
- __ - **api** - adicionar testes para as controllers
- _ok_ - **api** - adicionar swagger
- _ok_ - **webclient** - adicionar style/css
- __ - **webclient** - listagem e cadastro de locais de estoque para mercadoria
- __ - **webclient** - listagem e cadastro de tipos de mercadoria
- __ - **webclient** - listagem e cadastro de fabricantes
- _ok_ - **webclient** - exportar relatório para pdf
- _ok_ - **webclient** - adicionar gráfico no relatório
- _ok_ - **webclient** - página de relatório
- _ok_ - **docker** - debug python api no container
- _ok_ - **webclient** - cadastro de movimentacao de mercadorias
- _ok_ - **webclient** - listagem e cadastro de mercadorias
- _ok_ - **docker** - frontend
- _ok_ - **api** - criar rotas
- _ok_ - **api** - criar controllers
- _ok_ - **db** - criar tabelas
- _ok_ - **api** - criar data model objects
- _ok_ - **docker** - backend
- _ok_ - **docker** - database
