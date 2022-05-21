from abc import ABC, abstractmethod

class Bot(ABC):

    def __init__(self,nome, comandos):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def mostra_comandos(self):
        return self.__comandos

    def adicionar_comandos(self, comando, resposta):
        self.__comandos.adicionar_comandos(comando, resposta)

    def remover_comandos(self, comando):
        self.__comandos.remover_comandos(comando)

    def executa_comando(self,cmd):
        try:
            return self.__comandos.respostas_bot[cmd]
        except IndexError:
            print('Esse comando não existe')

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass