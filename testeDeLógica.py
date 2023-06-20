# Meu intuito aqui era testar uma lógica, o diálogo não é muito importante no momento.
respostavoceEstaAi = ('s') or ('sim')
voceEstaAi = str(input('Ei, depois de um minuto esperando algo acontecer você ainda está ai?')).lower()

if voceEstaAi != respostavoceEstaAi:
  print('sabia, bla bla bla')
else:
  print('nice')