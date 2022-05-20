from Bots.Bot import Bot

class BotEspanhol(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.comandos = {}
        self.comandos['1'] = ("Bom dia!", "iBienvenido! Como puedo ayudarte?")
        self.comandos['2'] = ("Qual seu taco favorito?", "Me gusta el pollo")
        self.comandos['3'] = ("Qual a sua cor favorita?", "Me gusta el azul")
        self.comandos['4'] = ("Adeus", "iHasta luego! Espero que vuelvas pronto")
        print(self.comandos)
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
 
    #def mostra_comandos(self):
    #    return self.comandos['a']
    
    def executa_comando(self,cmd):
        if cmd in self.comandos:
            return f"\nVocê --> {self.comandos[cmd][0]}\n{self.__nome} --> {self.comandos[cmd][1]}\n"
        else:
            return "No entiendo"

    def boas_vindas(self):
        return self.executa_comando('1')

    def despedida(self):
        return self.executa_comando('4')