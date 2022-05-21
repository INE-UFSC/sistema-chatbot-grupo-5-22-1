from Bots.Bot import Bot
from Comandos.Comandos import Comandos

class BotEspanhol(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.comandos = Comandos(['Bom dia', 'Qual seu taco favorito?', 
                                  'Qual a sua cor favorita?', 'Adeus'],
                                 ['iBienvenido! Como puedo ayudarte?', 'Me gusta el pollo',
                                  'Me gusta el azul', 'Espero que vuelvas pronto'])
        super().__init__(nome, self.comandos)

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"iHola! Soy el {self.__nome}"
    
    def boas_vindas(self):
        return self.executa_comando(0)

    def despedida(self):
        return self.executa_comando(3)