import random
import string

print("Bem vindo ao gerador de senhas do Pedro!")

def receber_comprimento():
    while True:
        comprimento = input("Escreva o comprimento de sua senha:")
        try:
            x = int(comprimento)
            if x >=6 and x <=60:
                print("Sua senha terá {} caracteres! Gerando senha...".format(comprimento))
                break
            else:
                print("Valor não pode ser abaixo de '6' ou maior que '60', tente de novo")
        except ValueError:
            print("Precisa ser um número, tente de novo")
    return comprimento

receber_comprimento()