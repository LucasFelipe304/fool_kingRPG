def pulaLinha():
  print()

def linhaDivisória():
  print('|','-' * 90,'|')

def informacoesPessoais():
  print('Informações Pessoais')


personagens = ("""I |Mago: Ewaelle
II|Guerreiro: Vorrus
III|Paladino: Raveneye""")
print(personagens)
pulaLinha()

escolhaDoPersonagem = str(input('------------> Escolha seu personagem: ')).upper()
if escolhaDoPersonagem == 'I':
  print('Você escolheu Ewaelle, o mago.')
  linhaDivisória()
  pulaLinha()
  pulaLinha()

  def infoMago():
    informacoesPessoais()
    pulaLinha()
    caracteristicas = {
      'Lugar de origem:':'Shadow Continent',
      'Altura:': '1.76',
      'Arma:': 'None',
      'Arcano:':'5',
      'Discernimento:':'4',
      'Percepção:':'5',
      'Medicina:':'3',
      'Saúde:':'2',
      'Iniciativa:':'4'
    }
    
    for chave, valor in caracteristicas.items():
      print(chave, valor)
  infoMago()

elif escolhaDoPersonagem == 'II':
  print('Você escolheu Vorrus, o guerreiro.')
  linhaDivisória()
  pulaLinha()
  pulaLinha()

  def infoGuerreiro():
    informacoesPessoais()
    pulaLinha()
    caracteristicas = {
      'Lugar de origem:':'Montanhas Rústicas de Glorinhidor',
      'Altura:': '1.83',
      'Arma:': 'Espada',
      'Arcano:':'-1',
      'Discernimento:':'2',
      'Percepção:':'3',
      'Medicina:':'0',
      'Saúde:':'4',
      'Iniciativa:':'5'
    }

    for chave, valor in caracteristicas.items():
      print(chave, valor)
  infoGuerreiro()