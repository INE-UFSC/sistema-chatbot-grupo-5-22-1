from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        #self.__nome nao esta como atributo no diagrama
        # self.__nome = nome
        self.__comandos = {'1' : ('Bom dia', 'Bom dia! Muito feliz de ter me chamado! :)'),
                           '2' : ('Qual o seu nome ?', 'Meu nome é BotFeliz, prazer! '),
                           '3' : ('Quero um conselho', 'Pegue sol! O dia está maravilhoso hoje! :D'),
                           '4' : ('Adeus', 'Até mais!! Tenha um bom dia!')}
        super().__init__(nome, self.__comandos)

#Esses metodos nao estao no diagrama UML entao estao como comentario
    # @property
    # def nome(self):
    #     return self.__nome

    # @nome.setter
    # def nome(self, nome):
    #     self.__nome = nome

    def apresentacao(self):
        return 'Oláa Meu nome é {}, muito feliz em ter me chamado!.'.format(self.nome)
 
    # def mostra_comandos(self):
    #     pass
    
    def executa_comando(self,cmd):
        if cmd in self.__comandos.keys():
            return self.__comandos[cmd][1]
        else:
            return 'Esse comando não existe'

    def boas_vindas(self):
        return '--> {} diz : Bem vindo!! O dia está muito lindo hoje!'.format(self.nome)

    def despedida(self):
        return '--> {} diz : Por favor não vá! Gosto muito de você!'.format(self.nome)