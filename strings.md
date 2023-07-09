# Strings
+ String é uma adeia de caracteres
+ cada elemento possui um índice
+ o primeiro elemento sempre terá índice 0
+ o índice deve ser especificado entre chavest

### Operações com strings
+ concatenação ```+```  
+ multiplicação ```*```  
+ composição ```%-rtd```  
  Onde:   
  ```-```: indica que o conteúdo deve ser exibido a partir do início da reserva. Se não especificado, o conteúdo é exibido a partir do final da reserva.  
  ```r```: é a reserva de espaço para o conteúdo  
  ```t```: é o tipo de variável  
  ```d``` número de casas decimais (para números reais)  

Exemplo: 
```
print("%-10.5f" % (8))
8.00000
```

### Fatiamento
```i```: início da fatia (se nenhum inteiro for especificado, o valor é 0)  
```j```: parada da fatia (se nenhum inteiro for especificado, o valor é o fim da fatia)  
```[i:j]```: fatia que inicia em ```i``` e para em ```j```  
índices negativos: -1 (último), -2 (penúltimo), ...
