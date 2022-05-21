#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotEspanhol import BotEspanhol
from Bots.BotEspelhado import BotEspelhado


###construa a lista de bots disponíveis aqui
bot1 = BotZangado("Yoda")
bot2 = BotFeliz("Julio")
bot3 = BotEspanhol("Joao")
bot4 = BotEspelhado("Odahlepse")
lista_bots = [bot1, bot2, bot3, bot4]


sys_bot = scb.SistemaChatBot('Grupo 5', lista_bots)
sys_bot.inicio()