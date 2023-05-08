# Uma função em Python é um bloco de código que realiza uma tarefa específica e pode ser reutilizado em diferentes partes de um programa. Essa tarefa pode incluir a execução de cálculos, operações de entrada e saída, processamento de dados e muito mais. Uma função é definida com a palavra-chave "def", seguida do nome da função, parâmetros de entrada entre parênteses e, opcionalmente, uma documentação da função, que descreve o que a função faz e quais são os parâmetros de entrada e saída. A função pode retornar um valor para o código que a chamou ou simplesmente realizar uma ação sem retorno de valor. Usando funções em Python, o código pode ser organizado, reutilizado e mantido de forma mais eficiente, facilitando a leitura e a depuração.

#É feita o código, dentro do prórprio "arquivo", como também pode ser feito em outro. Com isso, na parte que desejar utilizar a função, irá realizar o chamamento.


#Em python a função é iniciada com "def" - define(ir)  a função.
#Sem seguida se dará o "nome" da função, seguida de parênteses ":"

#Exemplo:

# def soma():
#   print("Imprimindo a função")

#Para chamar basta:

#soma()

#Ao executar o código, somente a linha 16 será executada, e irá ser feito o print com aquela saída. Assim, não precisaria escrever novamente o print.

#Utilizando variáveis e return na função:

# --- def soma():
#       txt = "imprimindo o resultado com variável"
#       return txt

# Para imprimir: print(soma())

#Neste caso o return está retornando o valor da variável para função que foi definida, só que o print só acontecerá neste caso se estiver printando a função.

#Funçao recursiva

#Ainda utilizando a função soma como exemplo:

# def soma(a, b):
#   c = a + b
#   return c
#
# print(soma(4, 9))

#----> 13

#Aqui definimos que ao se desejar somar números, basta dizer quais são os valores que deseja.
# Não irá precisar escrever aqueles códigos de soma, ou qualquer outro cálculo, por exemplo se fosse baskara.
# Bastaria criar a funçao com o cálculo e depois chamar informando os valores de cada variável e terá seu retorno.

#Existe variações possíveis:
# def soma(a, b, d):
#   c = a + b + d
#   if c % 2 == 0:
#       return "Par" 
#   else:
#       return "Ímpar"
# print(soma(4, 2, 10))
#
# --- > Par

#Aqui estamos criando um condicional dentro da funçao, definindo os valores no chamamento da função, para que nos retorne se é par ou impar, conforme está na função.
