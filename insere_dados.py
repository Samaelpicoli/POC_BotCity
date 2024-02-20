def inserir_comprador(bot, comprador):

    #Faz a navegação e insere o comprador

    if not bot.find( "inserir_pessoa", matching=0.97, waiting_time=30000):
        raise Exception('Não apareceu tela de inserir pessoa')

    bot.click_relative(165, 12)
    
    if not bot.find( "confere_janela", matching=0.97, waiting_time=10000):
        raise Exception('Não apareceu janela para inserir nome do associado')
    
    bot.click_relative(90, 55)
    bot.click_relative(97, 8)
    bot.paste(comprador)
    
    if not bot.find( "pesquisar", matching=0.97, waiting_time=10000):
        raise Exception('Não apareceu botão de pesquisar')
    bot.click()
    
    if not bot.find( "carregou_nome", matching=0.97, waiting_time=10000):
        raise Exception('Não carregou nome do associado')
    
    bot.click_relative(233, 391)

    return True


def inserir_vendedor(bot, vendedor):

    #Faz a navegação e insere o vendedor

    if not bot.find( "inserir_vendedor", matching=0.97, waiting_time=10000):
        not_found("inserir_vendedor")
    bot.click_relative(178, 9)
    
    if not bot.find( "inserir_nome", matching=0.97, waiting_time=10000):
        not_found("inserir_nome")
    bot.click_relative(93, 17)
    bot.paste(vendedor)
    
    if not bot.find( "pesquisar_vendedor", matching=0.97, waiting_time=10000):
        not_found("pesquisar_vendedor")
    bot.click()
    bot.wait(3000)
    
    if not bot.find( "selecionar_vendedor", matching=0.97, waiting_time=10000):
        not_found("selecionar_vendedor")
    bot.click()

    return True

def inserir_item(bot, codigo, quantidade, preco):

    #Faz a navegação e insere o código, preço e quantidade

    codigo = int(codigo)
    codigo = str(codigo)

    quantidade = int(quantidade)
    quantidade = str(quantidade)

    preco = str(preco)
    preco = preco.replace('.', ',')

    if not bot.find( "inserir_itens", matching=0.97, waiting_time=10000):
        not_found("inserir_itens")
    bot.click()   
    
    if not bot.find( "inserir_codigo", matching=0.97, waiting_time=10000):
        not_found("inserir_codigo")
    bot.click_relative(89, 14)
    bot.paste(codigo)
    bot.enter(wait=1000)

    bot.wait(2000)
    if not bot.find( "inserir_quantidade", matching=0.97, waiting_time=10000):
        not_found("inserir_quantidade")
    bot.click_relative(126, 11)
    bot.control_a()
    bot.paste(quantidade)
    bot.enter(wait=1000)

    if not bot.find( "inserir_valor", matching=0.97, waiting_time=10000):
        not_found("inserir_valor")
    bot.click_relative(155, 16)
    bot.control_a()
    bot.paste(preco)
    
    if not bot.find( "gravar_pedido", matching=0.97, waiting_time=10000):
        not_found("gravar_pedido")
    bot.click()

def insere_pagamento(bot):

    #Faz a navegação e insere o tipo de pagamento

    if not bot.find( "insere_pagamento", matching=0.97, waiting_time=10000):
        not_found("insere_pagamento")
    bot.click_relative(189, 10)
    
    if not bot.find( "escreve_codigo", matching=0.97, waiting_time=10000):
        not_found("escreve_codigo")
    bot.click_relative(121, 12)
    bot.paste('101')

    if not bot.find( "pesquisa_codigo", matching=0.97, waiting_time=10000):
        not_found("pesquisa_codigo")
    bot.click()
    
    if not bot.find( "seleciona_a_vista", matching=0.97, waiting_time=10000):
        not_found("seleciona_a_vista")
    bot.click()
    
    bot.wait(1000)
    
    if not bot.find( "seleciona_codigo", matching=0.97, waiting_time=10000):
        not_found("seleciona_codigo")
    bot.click()

def not_found(label):
    print(f"Element not found: {label}")

