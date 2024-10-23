import telebot # type: ignore
from telebot import types # type: ignore

# Conexión con nuestro bot
TOKEN = '7492175002:AAH_YNxMtm8LCgXmoe88EwwyiiE1pYGHWJU'
bot = telebot.TeleBot(TOKEN)

# Comando /start que despliega un menú con botones
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Crear el menú con botones
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Teclado ajustable
    btn1 = types.KeyboardButton('¿Qué es CCS?')
    btn2 = types.KeyboardButton('¿Qué es tarjeta blanca?')
    btn3 = types.KeyboardButton('¿A qué nos dedicamos?')
    btn4 = types.KeyboardButton('Precios')
    btn5 = types.KeyboardButton('Realizar un pedido')
    btn6 = types.KeyboardButton('Canales de información')
    btn7 = types.KeyboardButton('Garantias')
    btn8 = types.KeyboardButton('Referencias')

    # Agregar los botones al teclado
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    # Enviar mensaje con el teclado
    bot.send_message(message.chat.id, "Hola, ¿cómo puedo ayudarte? Selecciona una opción:", reply_markup=markup)

# Funciones para responder a las opciones seleccionadas
@bot.message_handler(func=lambda message: message.text == '¿Qué es CCS?')
def que_es_CCS(message):
    bot.reply_to(message, 'Son tarjetas de crédito con saldo para comprar en tiendas en línea, al adquirir una puedes sacar ganancias en productos, la preferencia de nuestros clientes se basa en artículos del hogar como: celulares, muebles, escritorios, aparatos electrónicos, componentes para computadoras, consolas de videojuegos y algunos artículos personales.')

@bot.message_handler(func=lambda message: message.text == '¿Qué es tarjeta blanca?')
def que_es_tarjeta_blanca(message):
    bot.reply_to(message, 'Para los que no saben que son las tarjetas blancas de este video son las CCs o llamadas también "Tarjetas Blancas" que en realidad son tarjetas clonadas de crédito la mayoría con buenos limites de crédito. Algunos se preguntan que Por qué no nos las quedamos Es sencillo, como sabemos las tarjetas de crédito solo dejan comprar mas no sacar efectivo lo cual no es tan factible para nosotros, es un cierto desgaste comprar y revender, se puede sacar buena ganancia pero el tiempo no nos da. Por lo cual optamos por vender las tarjetas y así tener tiempo para las CCS y venderlas el negocio es redondo y veloz, nuestros clientes ya conocen esto solo es para que los nuevos estén bien informados y no tengas preguntas y dudas de que si esto es un fraude ✅')

@bot.message_handler(func=lambda message: message.text == '¿A qué nos dedicamos?')
def a_que_nos_dedicamos(message):
    bot.reply_to(message, 'Yo me dedico al carding y preguntarán que es eso, pues el Carding es un término general para referirse a la utilización de los datos de las tarjetas de crédito robadas para beneficio personal, que puede consistir en la venta de los datos, en su utilización para comprar artículos. Hay que tener en cuenta que las CCs pueden utilizarse para hacer compras directas. Y ustedes no corren riesgo a nada, así que no se preocupen que nos les va a pasar nada. Como experiencia propia les puedo decir que en todos mis años sacando productos, nunca he tenido ningún problema, diariamente las páginas reciben miles de compras con tarjetas falsas y aún así pasa desapercibido la pregunta es, ¿por qué te buscarían a ti habiendo tanta gente que lo hace? Mi única recomendación es no abusar con las compras y nunca tendrán ningún problema. Después de lo explicado anteriormente, pues para los que se preguntan... ¿Qué hacemos? Pues les vendemos la CC a un precio muy accesible para que ustedes puedan comprar sus productos más baratos en Amazon o en cualquier otra página web con CCs Para las otras páginas web se usa el mismo método con las tarjetas.')

@bot.message_handler(func=lambda message: message.text == 'Precios')
def precios(message):
    bot.reply_to(message, 'PRECIO DE LAS CCS (A pesos mexicanos) $1000  x   $8000 / $1600  x   $15000 / $2500  x   $28500 / $3400  x   $40000 /')
    bot.reply_to(message, 'PRECIO DE LAS Tarjetas Blancas (A pesos mexicanos) $1000  x   $3000 / $1500  x   $5000 / $2500  x   $10500 / $3000  x   $15000')
    bot.reply_to(message, 'Para saber promociones Checa el Canal de Telegram o de WhatsApp')
                 
@bot.message_handler(func=lambda message: message.text == 'Realizar un pedido')
def realizar_un_pedido(message):
    bot.reply_to(message, 'Para realizar un pedido: @metodo_amazonx o a nuestro WhatsApp +52 7778247655')

@bot.message_handler(func=lambda message: message.text == 'Canales de información')
def canales_de_informacion(message):
    bot.reply_to(message, 'Puedes encontrarnos en nuestras canal de Telegram como: https://t.me/metodo_amazon y nuestro canal de WhatsApp como: https://whatsapp.com/channel/0029VagP4oK7j6gA7atHnK17')

@bot.message_handler(func=lambda message: message.text == 'Garantias')
def Garantias(message):
    bot.reply_to(message, '🚨 GARANTÍAS AL INVERTIR CONMIGO 🚨' 
                 '✅Experiencia y profesionalismo: Con confianza afirmo que mi gran experiencia y profesionalismo te permitirán alcanzar resultados exitosos al invertir conmigo.' 
                 '✅Honestidad y transparencia: 🔻Doy gran importancia a la honestidad y transparencia en cada una de nuestras referencias y trabajos. Tendrás la oportunidad de hacer el trabajo conmigo paso a paso, contribuyendo a la construcción de relaciones honestas y confiables con ustedes.' 
                 '✅Compromiso y responsabilidad: 🔻Mi reputación juega un papel crucial y estoy lista para escuchar todas sus preguntas. Recuerda que la decisión es completamente tuya, nosotros ni nadie tiene porque insistirte ni obligarte a comprar algo.')
@bot.message_handler(func=lambda message: message.text == 'Referencias')
def Referencias(message):
    bot.reply_to(message, 'Checa nuestro canal de Telegram de Referencias: https://t.me/Referencias_metodoamazonMx')

# Inicia el bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
