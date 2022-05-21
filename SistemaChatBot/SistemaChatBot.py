from Bots.Bot import Bot
from Bots.BotZangado import BotZangado


class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        for bot in lista_bots:
            if isinstance(bot, Bot):
                self.__lista_bots.append(bot)
        self.__bot = None
    
    def boas_vindas(self):
        print('Olá, esse é o sistema de chatbots do {} \n '.format(self.__empresa) )

    def mostra_menu(self):
        print('Os chat bots disponíveis no momento são :')
        for index, bot in enumerate(self.__lista_bots):
            print('Bot {} : {} - Mensagem de apresentação : {} '.format(index+1, bot.nome, bot.apresentacao()))
        print()

    def escolhe_bot(self):
        try:
            numero_bot = int(input('Selecione um bot : '))
            
            if numero_bot not in range(len(self.__lista_bots) + 1):
                print('Esse bot não existe')
            else:
                self.__bot = self.__lista_bots[numero_bot - 1]
                print(self.__bot.boas_vindas(), '\n')
        except ValueError:
            print('Digite um número válido para o bot')
        
    def mostra_comandos_bot(self):
        print('Os comandos são : ')
        comandos = self.__bot.mostra_comandos().comandos
        for index, comando in enumerate(comandos):
            print(index + 1 ,'-', comando)
        print()

    def le_envia_comando(self):
        try:
            cmd = int(input('Escolha um comando : '))
            if cmd == -1:
                print(self.__bot.despedida())
                return True
            else:
                print(f'--> {self.__bot.nome} diz :',
                    self.__bot .executa_comando(cmd - 1), '\n')
        except ValueError:
            print('Digite um número válido para o comando \n')
    
    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        if self.__bot != None:
            while True:
                self.mostra_comandos_bot()
                if self.le_envia_comando():
                    break

