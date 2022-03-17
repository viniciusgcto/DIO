from Televisao import Televisao   # Importando apenas a classe Televisão do arquivo Televisão.py (não vai executar o resto do arquivo)
from Televisao import teste       # Importando apenas o método teste (imprimir somente a palavra 'Teste')

televisao = Televisao() # Instanciando a classe numa variável
print(televisao.ligada) # Mostrando o status da TV
televisao.power()       # Ligando a TV   
print(televisao.ligada) # Atualizando o status

teste = teste()