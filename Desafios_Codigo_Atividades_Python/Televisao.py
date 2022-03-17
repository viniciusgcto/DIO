class Televisao:                 # Criando a classe Televisão
    def __init__(self):          # Inicializando a televisão desligada
        self.ligada = False      
    def power(self):             # Implementando botão liga/desliga
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

if __name__ == '__main__':   # Quando próprio arquivo é executado, nome é o 'main', se for chamado de fora, nome é diferente do 'main' (nome do arquivo) e não executa
    televisao = Televisao()  # Passando a classe para uma variável

    print('A televisão está ligada: {}'.format(televisao.ligada))       # Exibindo o status inicial (desligada)

    televisao.power()                                                   # Alterando status da TV

    print('A televisão está ligada: {}'.format(televisao.ligada))       # Exibindo o novo status

