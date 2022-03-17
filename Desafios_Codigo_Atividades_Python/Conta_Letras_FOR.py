# Objetivo: Retornar quantas letras cada palavra de determinada lista possui

def conta_letras(lista):
  contador = []                   # Lista vazia inicializada para receber o total de letras de cada palavra da lista

  for x in lista:                 # Para cada item da lista frutas (x)
    quantidade = len(x)           # Quantidade irá receber o tamanho do item - 'len' é o tamanho do item, por exemplo: uva tem 3 de cumprimento, 3 letras
    contador.append(quantidade)   # Lista contador será incrementada com as quantidades de letras em cada item da lista - 'append' coloca no final a variável
  return contador

if __name__ == '__main__':
  frutas = ["abacate", "banana", "tamarindo"] # Lista
  print(conta_letras(frutas))