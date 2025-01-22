#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://mundodosoleos.com")
except:
    print("O site Mundo dos oleos nào está acessível no momento.")
else:
    print("Conseguir acessar o site Mundo dos oleos com sucesso")

