from Bots.Bot import Bot
from Bots.BotZangado import BotZangado

inicio = True

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        for i in range(len(lista_bots)):
            if isinstance(lista_bots[i], Bot):
                self.__lista_bots.append(lista_bots[i])
        self.__bot = None
    
    def boas_vindas(self):
        print('Olá, esse é o sistema de chatbots do {} \n '.format(self.__empresa) )

    def mostra_menu(self):
        print('Os chat bots disponíveis no momento são :')
        x = 1
        for bot in self.__lista_bots:
            print('Bot {} : {} - Mensagem de apresentação : {} '.format(x, bot.nome, bot.apresentacao()))
            x += 1
        print()

    def escolhe_bot(self):
        bot = int(input('Selecione um bot : '))
        
        if bot > len(self.__lista_bots):
            print('Esse bot não existe')
        else:
            self.__bot = self.__lista_bots[bot - 1]
            print(self.__bot.boas_vindas(), '\n')
     
    def mostra_comandos_bot(self):
        print('Os comandos são : ')
        comandos = self.__bot.mostra_comandos().values()
        x = 1
        for i in comandos:
            print(x, '-', i[0],)
            x += 1
        print()

    def le_envia_comando(self):
        global inicio
        comando = input('Escolha um comando : ')
        if comando == '-1':
            inicio = False
            print(self.__bot.despedida())
        else:
            print('--> {} diz :'.format(self.__bot.nome),
                  self.__bot .executa_comando(comando))

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        if self.__bot != None:
            self.mostra_comandos_bot() 
            while inicio:
                self.le_envia_comando()

