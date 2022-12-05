import time
from Queue import Queue

Batata = Queue()

op = int(input("Digite a quantidade de pessoas na brinacadeira: "))
for n in range(op):
    pessoa = str(input("Adicione o nome da pessoa: "))
    Batata.push(pessoa)
while True:
    num = int(input("Digite a quantidade de vezes que quente será dito: "))
    print("Batata")
    for n in range(num):
        print("Quente")
        time.sleep(1)
        Batata.push(Batata.first.data)
        Batata.pop()
    print("Queimo!")
    print(Batata.first.data, "Foi queimado")
    Batata.pop()
    if Batata._size == 1:
        print(Batata.first.data, "ganhou a brincadeira")
        break

