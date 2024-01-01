# aqui vamos fazer o nosso primeiro projeto, que reconhece quando é passado um nome no parametro da função

def say_hi(name):
    if name == '':
        print("You didn't enter your name!")
    else:
        print("Hi there...")
        for letter in name:
            print(letter)

name = input("Your name: ")
say_hi(name)

# novidade: a função "input" espera que seja dado uma string para associar à uma variável, e assim continuar o a leitura do código.
# no nosso exemplo, ele mostra a mensagem para escrevermos o nome, e após escrever e dar um enter, ele associa o nome digitado à variável "name"
# então, ele chama a função que criamos "say_hi" atribuindo o nome escrito no parâmetro "name"