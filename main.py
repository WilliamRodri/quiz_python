from questions import *
import time
import os


def start():
    print("----------------------")
    print("------QUIZ PYTHON-----")
    print("----------------------")
    a = input("...PRESSIONE ENTER....")

    if a == "":
        quiz()
    else:
        print("PRECISA DAR UM ENTER")

def quiz():
    os.system('cls')
    nome = input("Digite seu nome: ").upper()

    pontuacao = 0

    print("----------------------")
    print("------QUIZ PYTHON-----")
    print("----------------------")

    print(questions[1])
    resposta1 = int(input("Digite sua resposta: "))

    if resposta1 == 1:
        pontuacao += 1
    else:
        pontuacao

    print(questions[2])
    resposta2 = int(input("Digite sua resposta: "))

    if resposta2 == 1:
        pontuacao += 1
    else:
        pontuacao

    print(questions[3])
    resposta3 = int(input("Digite sua resposta: "))

    if resposta3 == 1:
        pontuacao += 1
    else:
        pontuacao

    print(questions[4])
    resposta4 = int(input("Digite sua resposta: "))

    if resposta4 == 2:
        pontuacao += 1
    else:
        pontuacao

    print(questions[5])
    resposta5 = int(input("Digite sua resposta: "))

    if resposta5 == 2:
        pontuacao += 1
    else:
        pontuacao

    # ++5

    print(questions[6])
    resposta6 = int(input("Digite sua resposta: "))

    if resposta6 == 3:
        pontuacao += 1
    else:
        pontuacao

    print(questions[7])
    resposta7 = int(input("Digite sua resposta: "))

    if resposta7 == 3:
        pontuacao += 1
    else:
        pontuacao

    print(questions[8])
    resposta8 = int(input("Digite sua resposta: "))

    if resposta8 == 2:
        pontuacao += 1
    else:
        pontuacao

    print(questions[9])
    resposta9 = int(input("Digite sua resposta: "))

    if resposta9 == 3:
        pontuacao += 1
    else:
        pontuacao

    print(questions[10])
    resposta10 = int(input("Digite sua resposta: "))

    if resposta10 == 3:
        pontuacao += 1
    else:
        pontuacao

    print("AGUARDE...")
    time.sleep(1)
    print(pontuacao)

    taxaAcertos = pontuacao*10
    
    if pontuacao == 10:
        os.system('cls')
        print(f"{nome} PARABÉNS VOCÊ CONSEGUIR ACERTA TODAS AS PERGUNTAS!")
        print("TA CRAQUE EM PYTHON EM...")
        print(f"TAXA DE ACERTO: {taxaAcertos}%")
    elif pontuacao == 0:
        os.system('cls')
        print(f"{nome} PARABÉNS VOCÊ CONSEGUIR O FEITO DE ERRAR TODAS AS PERGUNTAS!")
        print("VAMOS ESTUDAR, SEMPRE A TEMPO.")
        print(f"TAXA DE ACERTO: {taxaAcertos}%")
    elif pontuacao >= 1 and pontuacao <= 3:
        os.system('cls')
        print(f"{nome} ESTUDE MAIS E TENTE NOVAMENTE O QUIZ!")
        print(f"TAXA DE ACERTO: {taxaAcertos}%")
    elif pontuacao >= 4 and pontuacao <= 6:
        os.system('cls')
        print(f"{nome} ESTUDE MAIS, SEI QUE DA MELHORAR!")
        print(f"TAXA DE ACERTO: {taxaAcertos}%")
    elif pontuacao >= 7 and pontuacao <= 8:
        os.system('cls')
        print(f"{nome} TA QUASE LÁ, VOCÊ CONSEGUE")
        print(f"TAXA DE ACERTO: {taxaAcertos}%")
    elif pontuacao == 9:
        os.system('cls')
        print(f"{nome} MUITO BOM!!! TA UM PASSO PRO 100% DE ACERTO")
        print(f"TAXA DE ACERTO: {taxaAcertos}%")

start()