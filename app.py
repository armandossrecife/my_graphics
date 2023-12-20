import entidades

class MeusGraficos():
  def __init__(self, descricao):
    self.descricao = descricao
    
  def f_grau1(self,x):
    return x+2
  
  def f_grau2(self,x):
      return x**2 - 2*x + 1
  
  def f_polinomio(self,x):
    return x**3 - 6*x**2 + 11*x - 6
  
  def mostra_grafico(self, funcao):
    if funcao is not None: 
      grafico_temp = entidades.Grafico()
      limite_inferior=-10
      limite_superior=10
      grafico_temp.criar_eixo_x(limite_inferior, limite_superior, 100)
      grafico_temp.calcular_y(funcao)  # Exemplo de uso da função seno do numpy
      grafico_temp.configura_titulo_e_rotulos(rotulo_x='x', rotulo_y='y')
      grafico_temp.configura_limites_dos_eixos(limite_inferior_x=limite_inferior, limite_superior_x=limite_superior, limite_inferior_y=limite_inferior, limite_superior_y=limite_superior)
      grafico_temp.exibir_grafico()
    else:
      print('Não foi passada a função para plotar o gráfico!')
  
  def menu_principal(self):
    print('1. Escolha a função')
    print('2. Mostrar o gráfico')
    print('3. SAIR')
  
  def menu_funcoes(self):
    print('1. Função do 1o. Grau')
    print('2. Função do 2o. Grau')
    print('3. Função Polinomial')
    print('4. SAIR')
  
  def chama_menu_funcoes(self):
    funcao = None
    while True:
      self.menu_funcoes()
      opcao = input('Qual a opção? ')
      if opcao=='1':
        funcao = self.f_grau1
        print('Função escolhida: 1o. Grau')
      elif opcao=='2':
        funcao = self.f_grau2
        print('Função escolhida: 2o. Grau')
      elif opcao=='3':
        funcao = self.f_polinomio
        print('Função escolhida: Polinomial')
      elif opcao=='4':
        break
      else:
        print('Opção Inválida!')
      return funcao
  
  def executa_programa(self):
    funcao = None
    while True:
      self.menu_principal()
      opcao = input('Qual a opção? ')
      if opcao=='1': 
        funcao = self.chama_menu_funcoes()
      elif opcao=='2':
        self.mostra_grafico(funcao)
      elif opcao=='3':
        break
      else:
        print('Opção Inválida!')