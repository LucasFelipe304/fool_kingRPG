# Meu objetivo é apenas fazer uma lógica simples com o while
from time import sleep

def todasAsPerguntas():
  perguntas = [
      ('Já pagou seus impostos?'),
      ('Já fez suas obrigações?'),
      ('Por que tanta revolta?'),
      ('Você me odeia?'),
      ('Porque tanto ódio?'),
      ('Por que você é assim?'),
      ('As pessoas vão te achar estranho, não vão?'),
      ('Você acha mesmo que comprar algumas coisinhas vão te tirar desse poço?'),
      ('Sua felicidade é momentânea, não acha?'),
      ('Você acha mesmo que alguém te entende?'),
      ('Você acredita mesmo que vai conquistar seus sonhos?'),
      ('E todas as suas paixões?'),
      ('Você ainda acha que é amado pelas pessoas?'),
      ('É serio que você ainda se acha importante para as pessoas? Puff...'),
      ('Você não cansa de se apaixonar, não é? Acha que isso vai te livrar dos sufocos? É uma maneira de se esconder'),
      ('Você não se encaixa em nenhum padrão da sociedade, ainda não percebeu?'),
  ]

  def IterarAsPerguntas():
    for pergunta in perguntas:
      print(pergunta)
      sleep(1)
  IterarAsPerguntas()

todasAsPerguntas()


