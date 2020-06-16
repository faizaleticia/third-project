# Tarefa

Escreva um programa que abra o arquivo clients.txt, que descreve em coordenadas geográficas normalizadas (longitude e latitude, ambas entre 0.0 e 1.0) um conjunto de clientes que devem ser atendidos por sete fornecedores. As coordenadas desses fornecedores são: A (0.0715, 0.5984), B (0.2336, 0.2094), C (0.0612, 0.8530), D (0.5088, 0.4992), E (0.5567, 0.8742), F (0.0944, 0.0894) e G (0.9028, 0.4606).

Inicialmente, é preciso fazer a visualização dos dados, ilustrando de alguma forma a distribuição de clientes e fornecedores, gerando uma imagem. Pede-se relacionar cada cliente a um único fornecedor, usando o critério de menor distância euclidiana entre eles. Uma vez feita essa associação, solicita-se exibir cada fornecedor e os códigos dos seus respectivos clientes, por ordem decrescente de distância (entre cada cliente e seu fornecedor).

## Tarefas
- [x] Ler arquivo de clientes
- [x] Ler arquivo de fornecedores
- [x] Relacionar clientes com fornecedores, usando o critério de menor distância euclidiana
- [x] Exibir cada fornecedor e os códigos dos seus clientes, por ordem decrescente de distância
- [x] Gerar imagem do resultado

## Resultados

O algoritmo gera para cada fornecedor um arquivo PDF com os códigos dos seus clientes, por ordem decrescente de distância euclidiana, bem como, um gráfico utilizando o Diagrama de Voronoi, o qual é um tipo especial de decomposição de um dado espaço, por exemplo, um espaço métrico, determinado pela distância para uma determinada família de objetos (subconjuntos) no espaço.

### Exemplo PDF

<img src="https://raw.githubusercontent.com/faizaleticia/third-project/master/assets/example/pdf.png?token=AHCXPPVB7LT2RJNT62SKDXS66KGUW" alt="PDF Example">

### Exemplo Gráfico

<img src="https://raw.githubusercontent.com/faizaleticia/third-project/master/assets/example/graph.png?token=AHCXPPWBBGLJQWNQMXROMFC66KG2K" alt="Graph Example">

