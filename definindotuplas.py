numero = (1,2,3,6,6,4,3,2,1,8,9,9,5,5,7,7,2,10,10)  #Para ser uma Tupla e preciso ser parenteses!
print ("Tupla original:", numero)
print("tamanho da Tupla:", len(numero))
print(numero[2])  #para mostrar o indice, lembrando que o (0) e o começo
print("fazendo o slicing do 2 ao 5", numero[2:5])  #o slicing nao pega o  ultimo item definido no recorte
print("Quantas vezes o numero repete o numero 8:", numero.count(8)) #O Count e usado para contar quantas vezes o numero desejado foi usado
print("posiçao da primeira ocorrencia do numero:", numero.index(7)) #O Index e usado para mostrar a primeira posiçao de ocorrencia do numero

minimo_tupla=min(numero)
print(minimo_tupla)

maximo_tupla=max(numero)
print(maximo_tupla)

sum_tupla=sum(numero)
print(sum_tupla)

tupla_ordenada=sorted(numero)
print(tupla_ordenada)

print("o numero 4 esta dentro da tupla!!!!", 4 in numero)

numero2=(15,20)
tupla_concatenada=numero+numero2
print("A concatenaçao das tuplas 1 e 2 resulta na nova tupla:",tupla_concatenada)

tupla_duplicada=numero*2
print(tupla_duplicada)


