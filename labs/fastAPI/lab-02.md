# Laboratório 2
Bem vindo! Aqui você vai juntar todos os conceitos vistos até aqui em uma prática que simula um cenário real onde você vai usar seus conhecimentos em docker para resolver sua tarefa.  

Você como menbro da Ceos Jr foi encarregado de testar a API de usuários que outro menbro fez para um projeto. A API utiliza Docker, logo, use seus conhecimento para subir o ambiente descrito no `docker-compose.yml` e faça alguns testes de CRUD na API.

> A API usada aqui foi retirada da [capacitação em fastAPI da Ceos](https://github.com/ernestogo99/fastAPI), se não viu ainda corre lá!

## Para a prática
Perceba que a primeira etapa desse laboratório se baseia na leitura, então separe um tempo para ver qual infraestrutura o projeto precisa como, bancos de dados e variáveis de ambiente.

Isso leva para a primeira etapa, o `.env.example` como o próprio nome diz é um exemplo, não `.env` real, então renomei o arquivo para pode usá-lo de maneira correta.

Outro ponto é que a API usa algo que não vimos em aula, que é o uso de variáveis de ambiente no docker compose, mas que não é muito complicado.  
Exemplo: `POSTGRES_DB=${DB_NAME:-mydatabase}`
- `DB_NAME` é o nome da variável no `.env`
- `:-mydatabase` é um nome padrão caso não consiga ler DB_NAME

Antes de hora de usar o compose faça o mesmo exercício mental de criar mentalmente o resultado final, visualizando cada container, evite só sair dando compose sem pensar. 

Agora podemos dar um `docker compose up -d`, o `-d` garante que não vamos ficar a com a tela cheia de logs dos containers. Mas sempre é útil ter logs a disposição para debuggar, então dê um `docker compose logs <NOME_SERVICO>` para acompanhar informações sobre os containers

Se fizer com o postgres você verá algo como:
```bash
postgres-1  | 2026-09-26 20:27:23.116 UTC [1] LOG:  database system is ready to accept connections
```

## Finalizando
Após testar a API e ver como tudo funcionou junto vamos usar `docker compose down -v` para finalizar a prática. Essa flag `-v` é para excluir tudo o que o compose gerou, deixando apenas as imagens para trás.