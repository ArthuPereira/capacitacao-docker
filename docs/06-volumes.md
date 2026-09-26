# Armazenamento com Volumes

## Guardando dados de um container
Já vimos que containers pode guardar vários tipos de serviços, mas também precisamos guardar informações deles, seja um banco de dados, arquivos.. Mas como fazer isso?

A arquitetura em camadas dos containers fornece uma solução inicial, o copy-write, mas ela não é muito útil, pois só guarda informação enquanto o container existe, logo um `docker rm` destrói todos os dados. A solução mais completa é criar ***volumes***.

## Volumes
A ideia de volumes é criar uma partição de armazenamento próprio, que sobrevive a morte do container e que pode ser facilmente apagada. Essa partição fica fora do container, em um caminho do sistema onde o próprio docker gerencia.

> Vale ressaltar que existem outras formas de armazenamento no docker, mas volumes são a mais comum e prática. As outras são Bind mounts e tmpfs mounts

Vamos agora para um cenário onde vamos criar e usar um volume, começamos criando um com:
```bash
docker volume create dados_db
```

Podemos verificar esse novo volume com `docker volume ls`, você verá algo como isso:
```
DRIVER    VOLUME NAME
local     24457ab58e63999091738b0827458a0bbfe723c9e51b6cb070c12cfb1bc4c4f6
``` 

> Para mais detalhes sobre o volume criado use docker inspect com o id do volume

E agora vamos subir um container com uma imagem de um banco de dados PostgreSQl:
```bash
docker run -d --name meu_postgres -p 5432:5432 -v dados_db:/var/lib/postgresql/data -e POSTGRES_PASSWORD=senha postgres
```

Dissecando o comando:
- `-p 5432:5432` mapeamento de portas, se não conhece veja o [laboratório 1](../labs/site-estatico/lab-01.md)
- `-v dados:/var...` é o mapeamento do volume para esse caminho, por sinal é o camimho mais comum para esse uso
- `-e POSTGRES_PASSWORD=senha` é uma variável de ambiente necessária para criar o container Postgres

Agora você pode se conectar a esse banco criado usando um Dbeaver ou outro cliente SQL de sua preferência, e pode testar também que apagar o container não apaga o banco de dados

<div align="center">
    <a href="./05-criando-imagens.md">←Voltar</a>
    <a href="./07-compose.md">Próximo→</a>
</div>