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

## Referências
+ GRUS, Joel. **Data Science do zero: primeiras regras com Python**. 2. ed. Rio de Janeiro: Alta Books, 2019
