# SupperSupply Solution


_OLD_
---

# Teste MStarSupply (Consultoria Morning Star)

## Prerequisitos
Ter o **docker** instalado e seu serviço rodando\
_referência da versão utilizada no desenvolvimento: **Docker version 25.0.4, build 1a576c5**_

## Executando a solução 
Dentro da pasta raiz do repositório, execute o seguinte comando em um terminal:\
`docker compose up --detach --build`\
**Para parar a execução:** `docker compose down`

## Endpoints dos componentes da solução
Com os containers rodando
- Banco de Dados MySQL: <root:root@localhost:5100/mstarsupply>
- API Backend: <http://localhost:5101/api/v0.1.0>
- API Documentação Swagger: <http://localhost:5101/apidocs>
- Frontend WebClient: <http://localhost:5102>

## Massa de dados de teste
Para recriar o banco de dados com os dados de teste acesse a seguinte URL da API: <http://localhost:5101/api/v0.1.0/init_test_db>

## Debugando no VSCode
Abrindo a pasta raiz no VSCode o arquivo `.vscode/launch.json` irá carregar a opção de DEBUG **"Python backend_api Remote Attach"** que se conecta com a porta especificada na api para o debugpy - com o container da API rodando, execute essa opção de debug no VSCode

