#Saber o tamanho da lista utilizando o LEN
minhalista = ["abacaxi", "morango", "laranja"]
minhalista2 = [0,1,2,3]
minhalista3 = ["abacaxi", 2, 9.89, True]
tamanho=len(minhalista)
print(tamanho)

#Adicionar informações na lista utilizando APPEND.
minhalista = ["abacaxi", "morango", "laranja"]
minhalista2 = [0,1,2,3]
minhalista3 = ["abacaxi", 2, 9.89, True]

minhalista3.append("Paloma")
print(minhalista3)

#Consultando se algo está na lista
minhalista = ["abacaxi", "morango", "laranja"]
minhalista2 = [0,1,2,3]
minhalista3 = ["abacaxi", 2, 9.89, True]

if "abacaxi" in minhalista:
  print("abacaxi esta na lista")

#Apagar elementos da lista: del
minhalista = ["abacaxi", "morango", "laranja"]
minhalista2 = [0,1,2,3]
minhalista3 = ["abacaxi", 2, 9.89, True]

del minhalista[2:]
print(minhalista)