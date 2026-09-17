# Principais Comandos

## Imagens
Como vimos, as imagens são os manifestos para criarmos containers, e é no [Docker Hub](https://hub.docker.com/) que achamos imagens oficiais dos desenvolvedores e empresas.

Vamos começar baixando a imagem do [Nginx](https://hub.docker.com/_/nginx), um servidor web, mas que também pode ser usado como proxy reverso, balanceador de carga e cache de HTTP. Vamos usar o seguinte comando:

```bash
docker pull nginx:alpine3.24
```

Explicando cada comando:  
- `docker pull` é o comando que busca e baixa uma imagem no docker hub  
- `nginx:alpine3.24` é o nome e tag da imagem que deve ser buscada.  

Tags são usadas para classificar imagens, como podem haver várias imagens de um mesmo serviço elas são usadas para rastrear versão e correções que ela aplica. No nosso caso `alpine3.24` informa que é uma imagem leve(típico de imagens alpine) na versão 3.24

Se você não informar versão, é usada automaticamente a versão *latest*, que é a mais atual.

---
Agora seria bom ver as imagens que baixamos, para isso vamos usar:  

```bash
docker images
```

Você deve ver algo como:  
```bash
IMAGE              ID             DISK USAGE   CONTENT SIZE   EXTRA
nginx:alpine3.24   c8497b180665        103MB         29.7MB        
nginx:latest       d0d674272be3        253MB         69.2MB 
```

Justo as imagens que baixamos no passo anterior, olhe com atenção as tags e a como a imagem alpine é mais leve(DISK USAGE).

>O comando docker run já baixa e inicia a imagem em um único comando, facilita se você já tem certeza da imagem a ser usada

## Containers
Chegou a hora de criar nossos primeiro container, vamos usar

```bash
docker run -d nginx
```
Isso vai iniciar um container com a imagem latest, `-d` é para não bloquear o terminal com as informações do nginx, teste sem par ver como fica.

Assim como fizemos com as imagens, vamos ver os containers que criamos com:

```bash
docker ps -a
```

O `-a` é para mostrar containers ligados e desligados(ou -all). Isso deve mostrar algo como:

```bash
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
d17c903bf547   nginx     "/docker-entrypoint.…"   11 seconds ago   Up 10 seconds   80/tcp    hopeful_bardeen
```


>Vale lembrar que rodar vários "run" vai criar vários containers com id's diferentes, aqui você pode ver isso

Isso informa coisas como o id do container(vamos usar isso), a imagem que ele usa, tempo de criação e o nome, que não é tão comum de usar. Agora também precisamos desligar o container, para isso:

```bash
docker stop <CONTAINER-ID>
```

Por isso precisamos do id do containers, operações como parar e inspecionar são feitas usando o id, vale lembrar que para ligar ele de volta o comando é:

```bash
docker start <CONTAINER_ID>
```

## Colocando em prática
Agora é sua vez, a ideia é que você use tudo isso e mais um pouco para ver docker sendo útil. Você deve iniciar um container usando uma imagem alpine de python, entrar no container e usar o python lá contido, teste coisas como:
- descubrir a versão do python;
- abrir o interpretador python;
- executar um pequeno código;

Uma dica é voltar aos primeiros passos, lá tem uma dica de como acessar o container.

## Limpando eventuais bagunças
Imagens e containers ocupam espaço, as vezes **muito espaço** a depender do projeto, por isso aqui vão comandos para ajudar a excluir o que não é mais usado:

Excluir imagem por id
```bash
docker rmi <IMAGEM-ID>
```
Excluir container por id
```bash
docker rm <CONTAINER-ID>
```

Excluir todas as imagens baixadas
```bash
docker rmi $(docker images -q)
```

Excluir todos os containers, ativos ou não
```bash
docker rm $(docker ps -aq)
```

<div align="center">
    <a href="./03-instalacao.md">←Voltar</a>
    <a href="./05">Próximo→</a>
</div>