x1 = 5.74
x2 = 5.72

# precisa de se instalar a biblioteca sigfig antes de correr o programa
# ex: 
#   pip install sigfig

from sigfig import round

def media(x1, x2, num_dig_sig):
    x1 = round(x1, sigfigs=num_dig_sig)
    x2 = round(x2, sigfigs=num_dig_sig)
    soma = round(x1+x2, sigfigs=num_dig_sig)
    media = round(soma/2, sigfigs=num_dig_sig)
    return media

print(media(x1, x2, num_dig_sig=2))
