#Bibliotecas utilizadas no processo
import pandas as pd
from botcity.core import DesktopBot

#Módulos do Processo
from login import login
import insere_dados as insere



#Esse processo irá ler uma planilha e fazer a inserção dos dados em um sistema desktop.
#Após concluir todos os pedidos, ele irá selecionar a forma de pagamento e concluir o pedido.

def main():
    
    #Realizando leitura do arquivo que já se encontra na máquina
    planilha = pd.read_excel(r"C:\Users\compr\Downloads\pedidos.xlsx")

    #instanciando a classe DesktopBot -> BotCity
    bot = DesktopBot()
    bot.execute(r"C:\Wonder\updater.exe")

    #A tela inicial as vezes demora um tempo para aparecer, bot aguardando
    if bot.find( "tela_abriu", matching=0.97, waiting_time=30000):
        tela_apareceu = True
        while tela_apareceu:
            if not bot.find( "tela_abriu", matching=0.97, waiting_time=10000):
                tela_apareceu = False
    
    #Login no sistema
    login(bot)
    
    #Aguardando botão aparecer para clicar
    if not bot.find( "lanca_pedido", matching=0.97, waiting_time=50000):
        not_found("lanca_pedido")
    bot.double_click_relative(32, -25)
    
    #Aguardando botão aparecer para clicar
    if not bot.find( "inserir_pedido", matching=0.97, waiting_time=10000):
        not_found("inserir_pedido")
    bot.click()

    #Faz a inserção dos dados da planilha, comprador, vendedor, código, quantidade e preço
    for index, linha in planilha.iterrows():
    
        insere.inserir_comprador(bot, linha['Nome Comprador'])
        
        insere.inserir_vendedor(bot, linha['Nome Vendedor'])
        
        insere.inserir_item(bot, linha['Código Produto'], linha['Quantidade'], linha['Preco Unitario'])
        
        bot.wait(1000)
    
        bot.alt_f4()

    #Insere o método de pagamento - sempre a vista     
    insere.insere_pagamento(bot)

    #Realiza o pedido e segue a navegação
    if not bot.find( "gravar_pedido", matching=0.97, waiting_time=10000):
        not_found("gravar_pedido")
    bot.click()
    
    if bot.find( "pedidos_abertos", matching=0.97, waiting_time=10000):
        bot.tab()
        bot.enter()

    if not bot.find( "imprimir_documento", matching=0.97, waiting_time=10000):
        not_found("imprimir_documento")
    bot.click_relative(273, 71)

    #Fechando sistemas
    bot.wait(1000)
    bot.alt_f4()

    bot.wait(1000)
    bot.alt_f4()

    bot.wait(1000)
    bot.alt_f4()
    
    print('Sucesso')

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()







