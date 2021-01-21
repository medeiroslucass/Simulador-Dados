import random
class SimuladorDeDado():
    def __init__(self):
        self.valor_minimo = int(input("Insira um valor minimo: "))
        self.valor_maximo = int(input("Insira um valor maximo: "))
        self.mensagem = "Você deseja rolar o dado? "
    def Gerar_dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        
    def Iniciar(self):
        resposta = input(self.mensagem).upper()
        
        if resposta[0] == "S":
            self.Gerar_dado()
            self.Iniciar()
        elif resposta[0] == "N":
            print("Foi bom jogar com você !! ^^.")
        else:
            print("Resposta Invalida. digite sim ou não")
            self.Iniciar()
simula = SimuladorDeDado()
simula.Iniciar()