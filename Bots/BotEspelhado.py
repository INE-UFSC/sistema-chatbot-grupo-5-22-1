from codeop import CommandCompiler
from Bots.Bot import Bot
from Comandos.Comandos import Comandos


class BotEspelhado(Bot):
    def __init__(self, nome):
        self.nome = nome
        self.comandos = Comandos(['Bom dia', 'Qual o seu nome ?', 'Quero um conselho'],
                                 ['aiD moB', f'{self.nome} é emon ueM', 
                                 'ohlepse on rahlo oa airros erpmeS'])
    
        super().__init__(nome, self.comandos)

    # nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    # nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    #@property
    #def comandos(self):
        #return self.comandos
        
    def apresentacao(self):
        # fazer o nome ser printado utilizando o self.__nome espelhado
        return "...odahlepse é olaf ue euq o odut ,odahlepsE toB o uos rorriM é emon uem ,álO"

    #def mostra_comandos(self):
    #    return self.comandos

    def boas_vindas(self):
        return "...odnalaf uotse euq o rednetne arap amelborp ahnet oãn euq orepse ,uehlocse em êcov abO"

    def despedida(self):
        return "...amixórp a éta ,raduja et redop mob otium ioF"