#FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFPICIO,
#INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.

from time import sleep #BIBLIOTECA PARA ESPERAR OS SEGUNDOS QUE VOCE DESEJA!
print("CONTAGEM REGRESSIVA!!!")
for num in range(10, -1, -1): # 0 -1,-1, É PARA QUE CHEGUE ATÉ 0.
    sleep(1) 
    print(num)
print("kabuuumm!!! Explode os Fogos de Artifício!!!")
