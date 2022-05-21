class Comandos:
    def __init__(self, comandos, respostas):
        self.__comandos = comandos
        self.__respostas_bot = respostas
    
    @property
    def comandos(self):
        return self.__comandos
    
    @property
    def respostas_bot(self):
        return self.__respostas_bot
  
    def adicionar_comandos(self, comando, resposta):
        self.__comandos.append(comando)
        self.__respostas_bot.append(resposta)
    
    def remover_comandos(self, comando):
        try:
            resposta = self.__respostas_bot[self.__comandos.index(comando)]
            self.__comandos.remove(comando)
            self.__respostas_bot.remove(resposta)
        except ValueError:
            print('Esse comando não existe')


