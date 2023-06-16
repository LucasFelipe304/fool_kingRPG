def pulaLinha():
  print()

def linhaDivisória():
  print('|','-' * 90,'|')

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
  print('Informações Pessoais')
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