# Python

## Ambientes Virtuais

`conda create -n <nome> python=<versão>`: cria\
`conda activate <nome>`: ativa\
`conda deactivate`: desativa\
`python -m pip install <pacote1> <pacote2>`: instala uma ou mais bibliotecas

*Exemplo*
```{r}
conda create -n censoInterno python=3.13
conda activate censoInterno
python -m pip install notebook matplotlib
jupyter notebook
python deactivate
```

## Espaços em branco
+ delimita trechos de código, geralmente é usado chaves ou colchetes pela maioria das linguagens de programação;
+ Python delimita trechos de código com o número de espaços;
+ preferencialmente utilize espaços e não tabulações;
+ barra invertida (/\) permite quebrar uma linha de código muito grande

## Módulos
`import <modulo>`: importa\
`import <modulo> as <alias>`: cria um alias\
`from matplotlib.pyplot import plot as pt, show as sw, title as tl`: importa biblioteca específicas com vários alias:

## Funções
+ Recebe nenhuma ou mais parâmetros;
+ Pode retornar ou não uma saída;
+ Podem ser atribuidas e inseridas como argumentos.
```{r}
def <nome>():
   return
```

*Exemplos*: a função `f` ao ser invocada com o parâmetro `exemplo` , passa para a sua definição o argumento `p` e retorna o seu conteúdo por meio de `return`.  
```{r}
def f(p):
   return parametro
f("exemplo")
```
+ Existem função *anônimas* também chamadas de anônimas. 
+ Muitos programadores consideram uma má prática de programação. 
+ Evite-as em códigos muito grandes pois pode tornar seu entendimento confuso

```{r}
x = 1
y = 2
soma = lambda y, x: x + y
soma(x,y)
```

## Strings (cadeia de caracteres)
+ Podem ser com aspas duplas ou simples, mas sempre aos pares;
+ a função `print` identifica codifica caracteres especiais por meio da barra invertida (/\);
```{r}
print("teste\tteste")
teste	teste
```
+ já o caractere `r` na frente das aspas cria uma *rawstring*, tudo é tratado como uma sequência de caracteres brutos ou crus, útil para análise de textos
```{r}
print(r"teste\tteste")
teste\tteste
```
+ `f"{}"`: permite exibir um texto de forma mais amigável e fluída.

```{r}
x = "Python"
y = "legal."

f"{x} é {y}"

'Python é legal.'
```

## Exceções
Recurso para tratar possíveis problemas temporários por exemplo, a divisão por zero
`ZeroDivisionError`: divisão por zero;\
`TypeError`: operação entre dados incompatíveis;\
`ValueError`: uma função recebe um argumento com o tipo correto, mas valor inadequado (converter string para inteiro);\
`IndexError`: erro ao acessar um índice inexistente;\
`KeyError`: erro ao buscar uma chave inexistente de um dicionário;\
`FileNotFoundError`: erro ao abrir/manipular um arquivo que não encontrado;\
`NameError`: erro ao usar uma variável que ainda não foi definida.
Exemplos
```{r}
try:
    0/0
except ZeroDivisionError:
    print("Divisão por zero.")
```
```{r}
try:
    0 / '0'
except TypeError:
    print("Operação entre diferentes tipos de dados")
```

## Listas
+ coleção ordenada por indices crescente;
+ sua composição pode ser homogênea (elementos do mesmo tipo) ou heterogênea;
+ a sua declaração é feito com um par de colchetes;
+ o seus elementos são indexados por um número, o primeiro elemento sempre terá índice zero;
+ o operador dois pontos especifica para o interpretador python que é uma faixa;
+ é possível acessar a lista em ordem decrescente;
+ o último elemento tem índice -1, penúltimo -2, antepenúltimo -3, ...
+ operador `in` permite verificar se o elemento está na lista
+ `.append()` adiciona um elemento na lista original;
+ `.extend()` extende a lista original, com outra lista
+ é possível adicionar duas listas, gerando uma terceira outra sem alterar a original (diferente de `.extende`), usando operador `+`
+ `.remove()` remove o elemento pelo conteúdo
```{r}
cesta = ["banana", "uva", "laranja", "morango", "abacaxi", "kiwi", "bergamota", "caqui"]

cesta[0]
'uva'

cesta[6]
'bergamota'

cesta[3:5]
['morango', 'abacaxi']

cesta[-1]
'caqui'

cesta[-5:-1]
['banana', 'uva', 'laranja', 'morango', 'abacaxi', 'kiwi', 'bergamota']

"uva" in cesta
True

cesta.extend(["melancia", "melão"])
cesta[7:]
['caqui', 'melancia', 'melão']

cesta.append("limão")

cesta1 = ["banana", "uva", "laranja", "morango"]
cesta2 = ["abacaxi", "kiwi", "bergamota", "caqui"]
cesta3 = cesta1 + cesta2

x, y = ["abacaxi", "kiwi"]
x,y
('abacaxi', 'kiwi')

x = ["abacaxi", "kiwi"]
x.remove("kiwi")
x
['abacaxi']
```

## Tuplas
+ São listas, porém não podem ser alteradas.
+ Mas podem ser copiadas para outras com novas tuplas
```{r}
tp1 = ("C", "Python", "Ruby", "R")
tp1
('C', 'Python', 'Ruby', 'R')

tp1 = ("C", "Python", "Ruby", "R")
tp2 = tp1 + ("C++", "Lua")
tp2
('C', 'Python', 'Ruby', 'R', 'C++', 'Lua')
```

## Referências
+ PYTHON SOFTWARE FOUNDATION. Python 3 Documentation. Disponível em: https://docs.python.org/3/. Acesso em: 21 maio 2026.
+ GRUS, Joel. **Data Science do zero: noções fundamentais com Python**. 2. ed. Rio de Janeiro: Alta Books, 2021.
