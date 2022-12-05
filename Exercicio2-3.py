from Stack import Stack

VerificarEx = Stack()

nãoAbre = False
expressão = str(input("Digite a expressão matematica: "))

for i in range(len(expressão)):
	if expressão[i] == '(':
		VerificarEx.push('(')
	if expressão[i] == ')' and VerificarEx._size > 0:
		VerificarEx.pop()
	elif expressão[i] == ')' and VerificarEx._size == 0:
            VerificarEx._size -= 1
            nãoAbre = True
            
		
if VerificarEx._size == 0:
	print("A expressão não viola a condição 1")
else:
	print("A expressão viola a condição 1")
if  nãoAbre == False:
    print("A expressão não viola a condição 2")
else:
	print("A expressão viola a condição 2")