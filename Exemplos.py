#Maioridade

# def maioridade(x):
#     n = x
#     if n < 18:
#         return "Menor de idade"
#     else:
#         return "Maior de idade"
    
# print(maioridade(int(input("Qual a sua idade: "))))




# Contagem

# def contagem():
#     for i in range(1, 11):
#         print(i)
#     for i in range(10, 0, -1):
#         print(i)

# contagem()

# O primeiro valor do "FOR" dentro do "in range" significa o início, o valor seguinte é o fim, na aparência de um terceiro valor, trata-se do incremento.

# Tem como fazer essa função contagem com função recursiva:

# def contagem(num):
#     if num > 0:
#         print(num)
#         contagem(num-1)
#         print(num)
#     else:
#         print(num)

# contagem(10)

#Uma função recursiva é uma função que chama a si própria durante sua execução. Dessa forma, quando uma função recursiva é executada, ela realiza uma chamada para si mesma, que, por sua vez, também pode realizar uma chamada para si mesma. 
#Esse processo continua até que ocorra uma condição de parada, que é chamada de caso base.
#Ao executar uma função recursiva, as chamadas são empilhadas na pilha de chamadas (stack), formando uma espécie de "pilha de operações". 
#Quando a função alcança o caso base, as chamadas começam a retornar, e a pilha de chamadas começa a ser "desempilhada", ou seja, as operações que foram empilhadas por último são as primeiras a serem executadas.
#Dessa forma, uma função recursiva pode criar um loop, já que a função pode ser chamada repetidamente, empilhando as chamadas na pilha de chamadas até que a condição de parada seja alcançada e as chamadas comecem a retornar.