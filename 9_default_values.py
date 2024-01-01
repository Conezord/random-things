# podemos criar uma função com valor padrão, caso nenhum parametro seja definido na chamada

def ola(name = 'aprendiz', location = 'Brasil'):
    print("Olá", name, "bem vindo ao", location)

ola()
ola(name='Fernando')
ola(location='Chile')
ola(name = "josé", location='México')

# nesse exemplo conseguimos identificar onde será substituído os parametros na frase original. 
# No caso de apenas chamar a função, ela vem com os parametros padrão estabelecidos previamente.