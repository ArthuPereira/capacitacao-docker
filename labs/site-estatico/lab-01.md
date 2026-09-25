# Laboratório 1
Bem vindo! aqui você vai praticar os conceitos da aula 4 e 5, criando uma imagem e executando um container com essa mesma imagem.

## Estrutura do laboratório
Esse é o ambiente que usaremos, nele temos um `Dockerfile` que define como criar a imagem e `/src` com arquivos de um site que será servido no container final.
```
/site-estatico
├── Dockerfile
├── lab-01.md
└── src
    ├── index.html
    ├── script.js
    └── style.css
``` 

## Prática
Usando a prática da aula 5 vamos criar a imagem a partir do dockerfile:

```bash
docker build -t site:ceos .
```

Dê um `docker images` para conferir a imagem listada junto das outras imagens do seu sistema. Agora para a execução do container vamos adicionar um novo conceito, o de mapeamento de portas.

A situação é a seguinte, o container gerado pela imagem tem um servidor web que serve o nosso site, por padrão um servidor web usa a porta 80 para comunicação(pelo menos http, mas isso não vem ao caso).  

O ponto é, ***containers são ambientes isolados do computador***, até mesmo na rede, então precisamos de um jeito de comunicar o servidor do container com o mundo exterior.  

Para isso usamos a porta 80(aquela declarada no `EXPOSE` do dockerfile) do servidor com uma porta nossa que esteja disponível, como a 8080 por exemplo

O comando para mapear as portas vai junto do `docker run`:

```bash
docker run -d -p 8080:80 site:ceos  
```

Com isso basta acessar `localhost:8080` e ver o site hospedado! Esse conceito de mapeamento de portas é essencial para quando formos usar bancos de dados e apis.

## Limpeza
Use alguns dos comandos da aula 4 para derrubar o container e excluir a imagem gerada

<div align="center">
    <a href="../../docs/05-criando-imagens.md">←Voltar</a>
    <a href="../../docs/06">Próximo→</a>
</div>