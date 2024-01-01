#agora vamos usar a função do exercicio anterior para perguntar infinitas vezes o nome
def say_hi(name):
    if name == '':
        print("You didn't enter your name!")
    else:
        print("Hi there...")
    for letter in name:
        print(letter)

while True:
    name = input("Your name: ")
    say_hi(name)
