# Anotações curso

## Para remover espaços em branco/vazios:
strip() -> Tiraa todos os espaços em branco do início e do fim da string;

lstrip() -> Tira todos espaços em branco, à esquerda;

rstrip() -> Tira todos espaços em branco, à direita.

## Regular Expression (RegEx)

É uma sequência de caracteres que forma um padrão de pesquisa.

RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado.

Regex segue alguns passos:

1 - Compilar um padrão;

2 - Comparar esse padrão com uma string;

3 - Verificar se retornou alguma combinação, se o padrão foi encontrado.

Quando utilizamos "(123)" dizemos para expressão regular que o valor tem que ser exatamente o que está dentro. Já quando usamos o "[1,2,3]", o a valor pode ser ou um ou outro.

O "?" é para dizer que posso ou não ter o valor.

## Quantificadores
Utilizamps para dizer quantas vezes um certo conjunto aparece naquele padrão;

Eles ter certo limite -> Um valor no conjunto pode aparecer de 0 até 1 vez.

## Ver dados de um objeto

dir(objeto) é um método embutido (built-in) que retorna uma lista de strings, com todos
os métodos e atributos do objeto que foi passado.


