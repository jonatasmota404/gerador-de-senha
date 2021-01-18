from random import choice, random
import string

def gerar_senha(tamanho, valores):
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)

    print(senha)


#gerar_senha(10, string.ascii_letters + string.digits + string.punctuation)