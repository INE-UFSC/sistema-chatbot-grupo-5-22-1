from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        #self.__nome nao esta como atributo no diagrama
        # self.__nome = nome
        self.__comandos = {'1' : ('Bom dia', 'Bom dia só se for para você!'),
                           '2' : ('Qual o seu nome ?', 'Tá surdo ?'),
                           '3' : ('Quero um conselho', 'Não tenho filho desse tamanho'),
                           '4' : ('Adeus', 'Finalmente, não aguentava mais!')}
        super().__init__(nome, self.__comandos)

#Esses metodos nao estao no diagrama UML entao estao como comentario
    # @property
    # def nome(self):
    #     return self.__nome

    # @nome.setter
    # def nome(self, nome):
    #     self.__nome = nome

    def apresentacao(self):
        return 'GRRRRR. Meu nome é {} e eu te odeio.'.format(self.nome)
 
    # def mostra_comandos(self):
    #     pass
    
    def executa_comando(self,cmd):
        if cmd in self.__comandos.keys():
            return self.__comandos[cmd][1]
        else:
            return 'Esse comando não existe'

    def boas_vindas(self):
        return '--> {} diz : Não posso acreditar qur você me escolheru. GRRRRRRR!'.format(self.nome)

    def despedida(self):
        return '--> {} diz : Espero nunca mais te ver de novo'.format(self.nome)