from Stack import Stack


pilha1 = Stack()
pilha2 = Stack()
pilha3 = Stack()
pilha4 = Stack()
pilhaC = Stack()
pilhaR = Stack()
def empilharC(codigo):
   
    if pilha1._size < pilha2._size and pilha1._size < pilha3._size and pilha1._size < pilha4._size and pilha1._size < 3 or pilha1._size == 0:
        print("Conteiner inserido na Pilha 1")
        pilha1.push(codigo)
        pilhaC.push(codigo)
    else:
            if pilha2._size < pilha1._size and pilha2._size <= pilha3._size and pilha2._size <= pilha4._size and pilha2._size < 3  or pilha2._size == 0:
                print("Conteiner inserido na Pilha 2")
                pilha2.push(codigo)
                pilhaC.push(codigo)
            else:
                    if pilha3._size < pilha2._size and pilha3._size < pilha1._size and pilha3._size <= pilha4._size and pilha3._size < 3  or pilha3._size == 0:  
                        print("Conteiner inserido na Pilha 3")    
                        pilha3.push(codigo)
                        pilhaC.push(codigo)
                    else:
                        if pilha4._size < pilha2._size and pilha4._size < pilha1._size and pilha4._size < pilha3._size and pilha4._size < 3  or pilha4._size == 0:
                            print("Conteiner inserido na Pilha 4")
                            pilha4.push(codigo) 
                            pilhaC.push(codigo)
                        else:
                            if pilha1._size == pilha2._size and pilha1._size == pilha3._size and pilha1._size == pilha4._size and pilha1._size < 3 and pilha1._size > 0:
                                print("Conteiner inserido na Pilha 1") 
                                pilha1.push(codigo) 
                                pilhaC.push(codigo)
                            else:
                                print("Todas as pilhas estão lotadas")  
def desempilharC(codigo):
    if codigo == pilha1.peek():
        print("Retirado da pilha 1")
        pilha1.pop()    
    if codigo == pilha2.peek():
        print("Retirado da pilha 2")
        pilha2.pop() 
    if codigo == pilha3.peek():
        print("Retirado da pilha 3")
        pilha3.pop() 
    if codigo == pilha4.peek():
        print("Retirado da pilha 4")
        pilha4.pop()     
    else:
        print("O container não pode ser removido")    
while True:
    ver = int(input("Digite '1' para empilhar um container ou '2'  para desempilhar \nDigite '3'para sair \n"))
    if ver == 3:
        break
    if ver == 1:
        verC = int(input("Digite o codigo do conteiner a ser empilhado \n"))
        if pilhaC._size == 0:
                print("Codigo", verC, "inserido")
                empilharC(verC)
                
        else:
            if verC == pilhaC.peek():
                print("Codigo invalido") 
            while verC != pilhaC.peek():
                pilhaR.push(pilhaC.peek())
                pilhaC.pop()
               
                if verC == pilhaC.peek() or pilhaC.peek() == None:
                    pilhaR.push(pilhaC.peek())
                    pilhaC.pop()
                    print("Codigo invalido")
                    for n in range (pilhaR._size):
                        pilhaC.push(pilhaR.peek())
                        pilhaR.pop()
                    break
                 
                if pilhaC._size == 0:
                    print("Codigo2", verC, "inserido")
                    empilharC(verC)
                    for n in range (pilhaR._size):
                        pilhaC.push(pilhaR.peek())
                        pilhaR.pop()
                    break
    if ver == 2:
        verR =  int(input("Digite o codigo do conteinr a ser removido \n"))
        if verR != pilhaC.peek():
            while verR != pilhaC.peek():
                pilhaR.push(pilhaC.peek())
                pilhaC.pop()
                if pilhaC._size == 0:
                    print("O codigo não existe")
                    
                    for n in range (pilhaR._size):
                        pilhaC.push(pilhaR.peek())
                        pilhaR.pop()
                    break
                if verR == pilhaC.peek():
                    desempilharC(verR)
                    for n in range (pilhaR._size):
                        pilhaC.push(pilhaR.peek())
                        pilhaR.pop()
                    break
        if verR == pilhaC.peek():
                    desempilharC(verR)
                    for n in range (pilhaR._size):
                        pilhaC.push(pilhaR.peek())
                        pilhaR.pop()
                           
