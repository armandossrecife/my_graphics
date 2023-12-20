import app

class Main:
  def __init__(self, app_graficos):
    self.app_graficos = app_graficos

  def executa(self):
    self.app_graficos.executa_programa()

meus_graficos =  app.MeusGraficos(descricao="Meus gráficos")
principal = Main(app_graficos=meus_graficos)
principal.executa()