from collections import deque

pilha=deque()
pilha.append("5")
pilha.append("6")
pilha.append("7")
pilha.append("8")
pilha.append("9")
pilha.append("10")
print(pilha)

pilha.pop() #soma os numeros
print(pilha)


soma=sum(int(x) for x in pilha)
print(soma)



from collections import deque

pilha=deque()
pilha.append("Lavar as louças")
pilha.append("lavar o banheiro")
pilha.append("Fazer o almoço")
pilha.append("Adicione ")

pilha.pop() #peça ao usuário para adicionar mais uma tarefa a pilha
print(input("Adicione mais uma tarefa"))
print(pilha)
