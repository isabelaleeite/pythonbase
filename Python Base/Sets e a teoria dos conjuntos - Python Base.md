## Set / Conjuntos

### Criar conjunto de python


**Conjunto de números** 

```
c1 = {1,2,3} 
c1 = set([1,2,3]) Utilizar essa sintaxe
```
* * *
Utilizar set para remover duplicados

```
conjunto_a = [1,2,3,4,5]
conjunto_b = [4,5,6,7,8]
```

### União

```
set(conjunto_a) | set(conjunto_b)
{1,2,3,4,5,6,7,8}
```

```
conjunto_a.union(conjunto_b)
{1,2,3,4,5,6,7,8}
```

### Intersessão 

```
conjunto_a.intersection(conjunto_b)

conjunto_a & conjunto_b
```

### Diferença

```
conjunto_a.difference(conjunto_b)
conjunto_a - conjunto_b
```

### Diferença Simétrica

```
conjunto_a.symmetric_difference(conjunto_b)

conjunto_a ^ conjunto_b
``` 


### Ver métodos

`dir(set)`

## Hash Table

### O(n)

Complexidade de comparacao de elementos

```
numeros = [1,2,3,4,5,1,1,1,7,,,,:, 8 ,9]

1 in numeros
True
```

### O(1) - constante 

Set implementa Hash Table

1 -> 0
2 -> 1 

 numeros = set([1,2,3,4,5,1,1,1,7,,,,:, 8 ,9])
 
 8 in numeros
 True
 

