from Bots.Bot import Bot
from Comandos.Comandos import Comandos

class BotZangado(Bot):
    def __init__(self,nome):
        #self.__nome nao esta como atributo no diagrama
        # self.__nome = nome
        self.__comandos = Comandos(['Bom dia', 'Qual o seu nome ?', 'Quero um conselho', 'Adeus'],
                                   ['Bom dia só se for para você!', f'Tá surdo ? Meu nome é {nome}', 
                                   'Não tenho filho desse tamanho', 'Finalmente, não aguentava mais!'])
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
    
    def boas_vindas(self):
        return '--> {} diz : Não posso acreditar que você me escolheu. GRRRRRRR!'.format(self.nome)

    def despedida(self):
        return '--> {} diz : Espero nunca mais te ver de novo'.format(self.nome)