# Condicionais

### IF
+ condicional obrigatória e pode ser inserida indefinidamente 
+ executa a cláusula pertencente ao condicional if, somente se a condicicional for verdeadeira;
+ Python utiliza a identação para criar estruturas hierarquicas entre os blocos de códigos;
```
>>> if 0 < 1:
...   print('ok')
... 
ok
```

### If-else
+ condicional opcional e únnica
+ executa a cláusula pertencente ao condicional if, somente se a condicicional for verdeadeira;
+ se for falsa, passa para a cláusula seguinte
+ 
```
>>> if 0 > 1:
...   print('ok')
... else:
...   print('no')
... 
no
```

### If-elif
+ Se hover muitas condicionais, a condicional ```elif``` deixará seu código mais organizado e legível
```
>>> if 0 >= 3:
...   print('0')
... elif 1 >= 3:
...   print('1')
... elif 2 >= 3:
...   print('2')
... elif 3 >= 3:
...   print('3')
... 
3
```

### Condicionais de uma linha
```
print(0) if 0 > 1 else print(1)
```
