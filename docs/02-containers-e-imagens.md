# Containers e Imagens

Vimos que o Docker consegue empacotar serviços em unidades chamadas containers, mas o que de fato são esses containers?

O container é uma unidade básica que o docker manipula, dentro dele você pode empacotar desde um SO, uma API, um banco de dados... e depois usar esse container para uma tarefa e desliga-lo como um programa qualquer.

Imagens são modelos de como criar um container de determinado serviço, como uma receita ou um molde. Em resumo com uma imagem você pode criar quantos containers quiser de um mesmo serviço.

Então como exercício mental pense que na Ceos começamos um novo projeto que usa uma API em python, todos precisam ter acesso a API para testar e desenvolver. Disponilizando uma imagem dela cada um poderia ter quantas cópias quisesse em vários containers.

Essa ideia de disponibilizar imagens é feita pelo [Docker Hub](https://hub.docker.com/), é de lá que pegamos as imagens oficiais dos serviços que vamos usar.

<div align="center">
    <a href="./01-o-que-e-docker.md">←Voltar</a>
    <a href="./03-instalacao.md">Próximo→</a>
</div>