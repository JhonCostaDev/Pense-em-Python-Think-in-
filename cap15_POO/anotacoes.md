# Classes e Objetos

Programação orientada a objetos utiliza-se de tipos definidos pelo programador.

No exemplo dado pelo o autor, é criada uma classe chamada Point, que representa um ponto no espaço bidimensional. Na notação matemática, os pontos muitas vezes são escritos entre parênteses, com uma vírgula  separando as coordenadas.

```python
# Exemplo
a = (0, 0)
b = (x, y)
```
## Criando a classe Point
Vide arquivo point.py
```python
class Point:
    """Representa dois pontos in um espaço 2D"""
```
A primeira linha indica que a nova classe se chama Point. Abaixo temos um **docstring** utilizado para explicar para que serve a classe.

### Curiosidade:
Se instanciamos um objeto da classe Point como ela está agora e executarmos, o python dará um retorno:
```bash
>>> <classes.point.Point object at 0x0000025D7F23CDA0>
```

O valor de retorno é uma referência a um objeto Point, qo qual foi atribuído a variável blank. Quando é exibida uma instância da classe, o Python diz a que classe ela pertence e a posição de memória onde a mesma está armazenada. O prefixo "0x" indica que os números na sequência estão em formato hexadecimal.

## Atributos


