#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotEspanhol import BotEspanhol
from Bots.BotEspelhado import BotEspelhado

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotFeliz("Julio"), BotEspanhol("Joao"), BotEspelhado("Odahlepse")]

sys_bot = scb.SistemaChatBot('Grupo 5', lista_bots)
sys_bot.inicio()