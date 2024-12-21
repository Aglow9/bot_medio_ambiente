import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
punto = 0
extra = False

@bot.event #nos logeamos
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(1309927026123346073)
    await channel.send('hola si no sabes que hacer introduce "$ayuda" para saber mis comandos!!!!') #ayuda

@bot.command()
async def ayuda(ctx):
    await ctx.send(f'mis comandos son los siguientes') #indica cuales son los comandos
    await ctx.send(f'$plastico, $plantas $preguntas, $puntos, $kioto')

@bot.command()
async def puntos(ctx):
    global punto
    global extra
    if punto < 50:
        await ctx.send(f"Puntos totales: {punto}")
    elif punto >= 50:
        await ctx.send(f"Puntos totales: {punto}  tienes mas de 50 desbloqueastes mas funciones!!!!!")

@bot.command() #2 preguntas sobre el plastico 
async def plastico(ctx):
    await ctx.send(f'escribe "1" si quieres saber con que materiales podemos remplazar el plastico. escribe "2" si quieres saber porque mucho de los plasticos acaban en el mar')
    def check(m): #leemos el mensaje
        return m.author == ctx.author
    mensaje = await bot.wait_for('message', check=check)
    respuesta_usuario = mensaje.content

    if int(respuesta_usuario) == 1: #comprobamos respuesta
        await ctx.send(f"exsiten materiales como los hongos que cuando se mesclan con residuos de agriculturas se puede emplear como plastico")
    elif int(respuesta_usuario) == 2:
        await ctx.send(f"acaba principalmente en el mar gracias a la bazuraleza terrestre que es transportada al mar gracias a fenomenos meteorologicos  ")
    else:
        await ctx.send("esa respuesta no es valida vuelve a preguntar!!!!")



@bot.command() #2 preguntas sobre cultivo de plantas
async def plantas(ctx):
    await ctx.send(f'escribe "1" si quieres saber como plantar un arbol o escribe "2" si quieres saber que plantas puedes cultivar en tu casa.')
    def check(m): #leemos el mensaje
        return m.author == ctx.author
    mensaje = await bot.wait_for('message', check=check)
    respuesta_usuario = mensaje.content

    if int(respuesta_usuario) == 1: #comprobamos respuesta
        await ctx.send(f"1.- primero elige un lugar donde la raices puedan crecer libremente")
        await ctx.send(f"2.- haz un hueco lo suficientemente grande para introducir todas la raices de la planta")
        await ctx.send(f"3.- despues planta el arbol en el agujero")
        await ctx.send(f"4.- y cubrelo de tierra y aplasta suavemente,")
        await ctx.send(f"5.- finalmente no se te olvide regar regularmente!!!!! ")
    elif int(respuesta_usuario) == 2:
        await ctx.send(f"puedes plantar cosas como los tomates cherry, zanahorias, pepinos, ajos, o guisantes ")
    else:
        await ctx.send(f"esa respuesta no es valida, vuelve a preguntar")

@bot.command()
async def kioto(ctx):
    await ctx.send(f"el protocolo de kioto propone que los paises mas industrializados se comprometan a cuidar el ambiente con su principal proposito siendo que reduscan los gases contaminantes")



    


@bot.command()
async def preguntas(ctx): #cuestionario de 10 preguntas aleatorio
    global punto
    global extra
    if punto >= 50:
        extra = True
    pregunta = random.randint(1, 10)
    await ctx.send(f"te enviare preguntas al azar algunas faciles y otras dificiles responderas escribiendo 1 , 2  o 3") #instrucciones
    if pregunta == 1:
        await ctx.send(f'que significan las "tres R" ') # pregunta 1
        await ctx.send('1: (rehacer reusar reciclar) 2: (reducir reutilizar reciclar)  3:(reparar reutilizar reciclar)') #respuestas

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 2: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos

            with open('images/3 R.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)
            if extra == True:
                await ctx.send(f"https://concepto.de/las-tres-r/")
        else: #si la respuesta no es la correcta
            await ctx.send(f"incorrecto!!!")

    elif pregunta == 2: #pregunta 2
        await ctx.send(f"¿como acaba la basura en el mar?")
        await ctx.send(f'1:(la basura es tirada al mar directamente) 2:(gracias a que tiramos la basura por la taza) 3:(gracias a fenomenos meteorologiocos)')

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 3: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos
            with open('images/basura_oceano.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)
            if extra == True:
                await ctx.send(f"https://www.iberdrola.com/sostenibilidad/como-llega-el-plastico-al-mar")

        else: #si la respuesta no es la requerida
            await ctx.send(f"incorrecto!!!")

    elif pregunta == 3: #pregunta 3
        await ctx.send(f"¿Por qué es importante de reciclar")
        await ctx.send(f'1:(para no contaminar el ambiente)  2:(porque tanta basura se ve fea)  3:(porque el envase de los productos me lo indica)')

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 1: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos
            if extra == True:
                await ctx.send(f"https://www.nationalgeographicla.com/medio-ambiente/2023/05/que-beneficios-nos-trae-el-reciclaje-5-datos-que-necesitas-saber")

            with open('images/medio_ambiente.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)

        else: #si la respuesta no es la requerida
            await ctx.send(f"incorrecto!!!")


    elif pregunta == 4: #pregunta 4
        await ctx.send(f"Cuáles son algunas de las consecuencias del cambio climático?")
        await ctx.send(f'1:(el aumento de la biodiversidad) 2:(el aumento de la temperatura 3:(aumento en la calidad de la salud))')

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 2: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos

            with open('images/cambio_climatico.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)
            if extra == True:
                await ctx.send(f"https://www.nationalgeographicla.com/medio-ambiente/2024/10/cabernet-sauvignon-malbec-nebbiolo-o-zinfandel-cual-es-la-diferencia-entre-estas-variedades-de-uva-que-crecen-en-mexico")

        else: #si la respuesta no es la requerida
            await ctx.send(f"incorrecto!!!")

    elif pregunta == 5: #pregunta 5
        await ctx.send(f"¿En qué consiste el protocolo de Kioto?")
        await ctx.send(f'1:(en reducir la cantidad de emisiones de gases), 2:(en aumentar el uso de combustibles fosiles)  3:(en reducir el uso de los plasticos)')

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 1: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos
            with open('images/protocolo_kioto.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)
            if extra == True:
                await ctx.send(f"https://www.ecologiaverde.com/protocolo-de-kioto-que-es-y-en-que-consiste-413.html")

        else: #si la respuesta no es la requerida
            await ctx.send(f"incorrecto!!!")



    elif pregunta == 6: #pregunta 6
        await ctx.send(f"¿Cuáles son las principales fuentes de contaminación del agua?")
        await ctx.send(f'1(la quema de basura en la ciudad 2:(la sobrepesca) 3: (Aguas residuales urbanas)')

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 3: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos
            with open('images/aguas_residuales.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)
            if extra == True:
                await ctx.send(f"https://www.fundacionaquae.org/wiki/los-residuos-que-mas-contaminan-el-agua/")

        else: #si la respuesta no es la requerida
            await ctx.send(f"incorrecto!!!")

    elif pregunta == 7: #pregunta 7
        await ctx.send(f"cual de estos es un ejemplo de desastre ecológico")
        await ctx.send(f'1(un terremoto) 2(Incendios forestales)  3(un tornado)')

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 2: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos
            with open('images/incendio_forestal.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)
            if extra == True:
                await ctx.send(f"https://www.bioguia.com/mercado/peores-desastres-ambientales-del-mundo_94583573.html")

        else: #si la respuesta no es la requerida
            await ctx.send(f"incorrecto!!!")
    


    elif pregunta == 8: #pregunta 8
        await ctx.send(f" ¿Qué es la energía renovable?")
        await ctx.send(f'1(es aquella que se obtiene de medios naturales) 2(aquella que se obtiene del carbon) 3(la energia que proviene de la fotosintesis)')

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 1: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos
            with open('images/energias_renovables.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)
            if extra == True:
                await ctx.send("https://www.un.org/es/climatechange/what-is-renewable-energy#:~:text=La%20%EE%80%80energ%C3%ADa%20e%C3%B3lica%EE%80%81%20aprovecha")

        else: #si la respuesta no es la requerida
            await ctx.send(f"incorrecto!!!")


    elif pregunta == 9: #pregunta 9
        await ctx.send(f"¿Qué es la desertificación?")
        await ctx.send(f'1(es cuando se expande un desierto) 2(es el proceso cuando la tierra se seca debido a la falta de agua)   3(es el proceso cuando la tierras fertiles se degradan y se convierten en desierto)')

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 3: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos
            with open('images/desertificacion.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)
            if extra == True:
                await ctx.send(f"https://www.iberdrola.com/sostenibilidad/desertificacion")

        else: #si la respuesta no es la requerida
            await ctx.send(f"incorrecto!!!")

    elif pregunta == 10: #pregunta 10
        await ctx.send(f"¿Qué se puede hacer para reducir las emisiones de gases de efecto invernadero?")
        await ctx.send(f'1(dejar de usar combustibles fosiles) 2(aumentar el uso de energias nucleares) 3(reducir las campañas de reciclaje)')

        def check(m): #leemos el mensaje del usuario
            return m.author == ctx.author
        mensaje = await bot.wait_for('message', check=check)
        respuesta_usuario = mensaje.content

        if int(respuesta_usuario) == 1: #comprobamos si es la respuesta es correcta
            await ctx.send(f"correcto ganaste 5 puntos!!!")
            punto+=5 #damos puntos
            with open('images/combustibles_fosiles.jpg', 'rb') as f: #enviamos imagen!!!
                picture = discord.File(f)
            await ctx.send(file=picture)
            if extra == True:
                await ctx.send(f"https://www.fundacionaquae.org/wiki/los-residuos-que-mas-contaminan-el-agua/")

        else: #si la respuesta no es la requerida
            await ctx.send(f"incorrecto!!!")

bot.run("TOKEN")