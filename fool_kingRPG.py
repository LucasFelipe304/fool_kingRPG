from time import sleep
from random import randint, choice
from string import ascii_letters

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
  pulaLinha()
  pulaLinha()
  pulaLinha()

  print("""Depois de mais uma longa noite de procura pela tumba perdida do Rei Tolo, você acorda sob o que parece ser uma pilha de pedras.""")
  print("""Uh! O que é isso? onde estou?""")
  
  desejaUtilizarIndividualidadeRadiante = str(input('Deseja utilizar *Individualidade Radiante*? [S/N] ')).upper()

  if desejaUtilizarIndividualidadeRadiante == 'S':
    print("""Sem muitas opções, você decide usar sua magia "Individualidade Radiante" para iluminar o seu redor...""")
    print("""Seu feixe de luz faz um barulho estrondoso por conta da ressonância provinda do lugar, te deixando com medo e ansioso naquele imenso corredor escuro, aparentemente sem fim.""")
    sleep(2.5)
    print("""Após todo o barulho passar, tochas acendem pelas paredes extensas daquele lugar. Olhando para trás tudo que você vê é uma imensa parede de concreto, uma pilha de ossos e no teto, um desenho de um circulo branco.""")
    sleep(5)
    print("""Aterrorizado com tudo aquilo, você decide andar por todo aquele corredor em busca de uma saída.""")
    sleep(3)
    print("""Depois de algum tempo andando sem parar e incomodado com tudo aquilo, você se sente perseguido e ameaçado...""")

    desejaEntrarEmPosicaoDeCombate = str(input('Deseja entrar em posição de combate? [S/N] ')).upper()

    if desejaEntrarEmPosicaoDeCombate == 'S':
      print("""Com toda a sua iniciativa e experiência no Shadow Continent, você pretende enfrentar aquela suposta criatura mesmo não sabendo o lugar certo por onde ela vem.""")
      sleep(5)
      vozDaCriaturaApresentacao = ("""Poxa...ainda nem nos conhecemos direito e você quer me atacar?""")
      print(vozDaCriaturaApresentacao)
      sleep(2.5)
      print("""Você até tenta utilizar seu *Véu Sombrio* como forma de defesa pessoal mas a criatura avança em sua direção em um piscar de olhos, te deixando atordoado e te fazendo adormecer.""")
      sleep(7)
      print("""Depois de parte do efeito de atordoamento acabar, porém com uma forte dor de cabeça, você acorda sendo arrastado.""")
      sleep(5)
      print("""Todo o lugar a sua volta é branco, como se fosse um enorme cubo. As paredes tinham divisórias pretas, deixando aquele lugar ainda mais confuso e enorme.""")
      sleep(5)
      print("""Sua vista está embaçada, você não consegue ver o que está te arrastando. A última coisa que você percebe naquele lugar estranho é uma porta se fechando bem na sua frente.""")

    else:
      print("""Mesmo com medo, você decide manter a calma e ser vigilante...""")
      vozDaCriaturaApresentacao = ("""Você é o único que me ouviu e manteve o total controle de si mesmo - Exclama uma voz comúm pelo vasto corredor daquele lugar.""")
      sleep(5)
      print(vozDaCriaturaApresentacao)
      print("""Q-quem-""")
      sleep(3.5)
      
      def bugMode():
          contador = 0
          while True:
            letraAleatoria = choice(ascii_letters)
            numeroAleatorio = randint(0, 9)
            contador += 1
            print(numeroAleatorio, letraAleatoria, end='')
            if contador == 9999999:
              break

      pulaLinha()
      sleep(10)
      pulaLinha()
      print('...')
      print('Você')

      
      bugMode()
      
  else:
    print("""Ainda confuso, você espera algo acontecer...""")
    sleep(5)
    print("""Se passando algum tempo e sem algum movimento, você decide tentar chamar a atenção de alguém:""")
    sleep(2.5)
    print('Oi! - sua voz ecoa')
    sleep(2.5)
    print("""No mesmo instante, tochas se acendem por aquele lugar ressoante e você percebe onde está: É um imenso e largo corredor, aparentemente sem fim.""")
    sleep(3)
    print("""Olhando atrás de você, é visto uma pilha de ossos e uma imensa parede de concreto. No teto há um esquisito desenho de um circulo branco.""")
    sleep(5)
    print("""Sem outra saída, você decide andar por todo aquele silencioso corredor...""")
    sleep(5)
    print("""Após um tempo, é evidente que você não está sozinho. Olhando para os cantos por detrás de você, é visto olhos pequenos, amarelos e sem retina por volta de uma silhueta.""")
    sleep(5)
    print("""Extremamente perturbado, você corre corre em busca de alguma saída. Não há como você lutar, suas mãos estão congeladas de tamanho medo...""")
    sleep(5)
    print("""Após um tempo correndo, você não percebe mais nada te perseguindo, porém dá de cara com um imenso muro, dividindo dois outros caminhos escuros.""")
    sleep(5)
    print("""O caminho da esquerda é um pouco mais iluminado, porém não é possível ver o seu fim. Em contrapartida, o da direita é totalmente escuro, mas há uma pequena lamparina sob uma porta branca.""")
    sleep(8)
    print("""Antes que seja possível decidir por qual caminho ir, você é supreendido pelo alto som de passos atrás de você...""")
    sleep(5)
    print("""Virando para trás e preparado para se defender, tudo ao seu redor parece congelar. No caminho da direita aquela porta finalmente se abre, te mostrando o que parece ser um quarto comúm.""")
    

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