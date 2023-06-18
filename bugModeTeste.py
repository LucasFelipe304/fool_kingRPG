from random import randint, choice
from string import ascii_letters
from time import sleep

def bugMode():
  contador = 0
  while True:
    letraAleatoria = choice(ascii_letters)
    numeroAleatorio = randint(0, 9)
    contador += 1
    print(numeroAleatorio, letraAleatoria, end='')
    if contador == 999:
      break
  print()
  sleep(10)
  print()
  print('...')
  print('Você')


bugMode()