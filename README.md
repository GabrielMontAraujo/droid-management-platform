# Droid Management Platform

O Droid Management Platform é uma solução completa para o gerenciamento de droids, incluindo uma API robusta, CI/CD com Docker e Kubernetes, e uma interface de usuário baseada em React para facilitar o controle e monitoramento dos seus droids.

## Características

- **API de Gerenciamento de Droids:** Uma API RESTful construída com FastAPI para gerenciar todas as operações relacionadas aos droids, como adição, remoção, atualização e consulta de informações.

- **CI/CD com Docker e Kubernetes:** Integração contínua e implantação contínua usando Docker para empacotar o aplicativo e Kubernetes para orquestrar e gerenciar os contêineres em escala.

- **Frontend em React:** Uma interface de usuário moderna e responsiva construída com React para interagir com a API e visualizar dados sobre os droids.

## Como Usar

### Pré-requisitos

- Python 3.x
- Docker
- Kubernetes

### Configuração

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/droid-management-platform.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd droid-management-platform
    ```

3. Instale as dependências do Python:

    ```bash
    pip install -r requirements.txt
    ```

### Execução

1. Inicie a API de Gerenciamento de Droids:

    ```bash
    uvicorn main:app --reload
    ```

2. Inicie o frontend React (substitua <endereço-da-api> pelo endereço onde a API está sendo executada):

    ```bash
    cd frontend
    npm install
    REACT_APP_API_URL=http://<endereço-da-api> npm start
    ```

3. Acesse o frontend em seu navegador:

    ```
    http://localhost:3000
    ```

## Contribuição

Se você encontrar algum problema ou tiver sugestões para melhorar o Droid Management Platform, sinta-se à vontade para abrir uma issue ou enviar um pull request.
