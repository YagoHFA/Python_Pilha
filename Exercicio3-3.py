from Queue import Queue
import random

FilaN = Queue()
FilaP = Queue()
cont  = 0
while True:
    opção = int(input("Se você  tem de 20 á 49 anos digite '1'\nSe você tem mais de 50 digite '2'\nDigite '3' para sair \n"))
    if opção == 1:
        senha = 'N' + str(random.randint(1, 10))
        print("Sua senha é: ", senha)
        FilaN.push(senha)
    if opção == 2:
        senha = 'P' + str(random.randint(1,10))    
        print("Sua senha é: ", senha)
        FilaP.push(senha)
       
    if opção == 3:
        break
if FilaP._size == 0:
    for n in range(FilaN._size):
        print("A senha ", FilaN.peek(), " foi chamada")
        FilaN.pop()
else:
    count = 0
    while FilaP._size > 0:
        
        print("A senha ", FilaP.peek(), "foi chamada")
        FilaP.pop()
        count += 1
        if count == 3:
            print("A senha ", FilaN.peek(), " foi chamada")
            FilaN.pop()
            count = 0 
    if FilaP._size == 0:
        for n in range(FilaN._size):
            print("A senha ", FilaN.peek(), " foi chamada")
            FilaN.pop() 

