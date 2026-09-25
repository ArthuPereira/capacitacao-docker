# Criando imagens com Dockerfile

## O que é um Dockerfile?
Como já vimos, imagens são instruções de como criar determinado container, mas como definir essas instruções? `Dockerfile` são arquivos que defime para a composição de uma imagem, normalmente encontramis uma imagem base, código que o container vai guardar e executar além de dependências extras.

## Criando o Dockerfile
Os comandos mais comuns para escrevmos dockerFile são:
- `FROM` para informar qual imagem usaremos como base
- `RUN` para comandos que irão afetar a infraestrutura do sistema  nesse ambiente
- `COPY` é usado para copiar arquivos locais para o ambiente interno da imagem
- `CMD` para informar qual comando será executado por padrão
- `EXPOSE` para declarar em quais portas de rede o aplicativo dentro do contêiner vai escutar durante a execução

> Imagens base dizem respeito a uma característica das imagens docker, elas são baseadas em camadas. Assim é possivel "encaixar camadas" para criar novas imagens, as bases mais comuns são SO's e linguagens de programação

Vamos ver um exemplo para deixar mais claro:
```Dockerfile
FROM ubuntu:16.04
RUN apt-get update && apt-get install nginx -y
COPY arquivo_teste /tmp/arquivo_teste
CMD bash
```

Isso cria uma imagem, sua base é o Ubuntu 16.04, esse ubuntu vai estar atualizado e com `nginx` instalado. O `arquivo_teste` será copiado para `/tmp/arquivo_teste` dentro do container gerado e por fim o container gerado abre o bash

Outro exemplo, mas agora tente definir você qual será o resultado
```Dockerfile
FROM nginx:alpine

COPY ./src /usr/share/nginx/html

EXPOSE 80
```

## Executando o Dockerfile
O principal comando para criar imagens é o `docker build`, um exemplo de uso é esse:

```bash
docker build -t site:ceos .
```

Explicando os outros termos:
- `-t` declara que o próximo termo é o nome da imagem
- `site:ceos` é o conjunto repositório e tag da imagem que será criada, o nome da imagem
- `.` define que o caminho para o dockerfile, nesse caso ele está na mesma pasta que o comando é executado

Para praticar os conceitos vistos vá para o [Laboratório 1](../labs/site-estatico/lab-01.md), onde você pode criar e executar uma imagem de um site estático.

<div align="center">
    <a href="./04-comandos.md">←Voltar</a>
    <a href="./06">Próximo→</a>
</div>