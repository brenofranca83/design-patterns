# Exercício de Padrões de Projeto

Enunciado: Você foi contratado para desenvolver um módulo de cálculo de frete para um sistema de e-commerce. O sistema deve ser capaz de calcular o custo de envio de diferentes transportadoras, dependendo:
- Do tipo de envio selecionado pelo usuário (ex.: Sedex, PAC, Transportadora privada, Retirada na loja).
- Da estratégia de cálculo adotada por cada transportadora (ex.: por peso, por distância, taxa fixa, etc).

Para manter o sistema extensível e facilitar a adição de novas transportadoras e formas de cálculo, implemente a solução combinando dois padrões do catálogo GoF, um criacional e um comportamental.

Para entendimento da solução implementada em Python, iniciar a navegação pelo cliente, que interage com uma implementação de uma "fábrica" de entregas. Em seguida, a fábrica entrega o seu "produto", que são os vários formatos de entrega, com várias implementações. A empresa possui estratégias para cálculo do frete.
