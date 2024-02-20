def login(bot):
    #Realiza login no sistema
    if not bot.find( "insere_senha", matching=0.97, waiting_time=30000):
        raise Exception("insere_senha")
    bot.click_relative(90, 14)

    bot.control_a()

    bot.paste('1958')

    if not bot.find( "conectar", matching=0.97, waiting_time=10000):
        raise Exception("conectar")
    bot.click()