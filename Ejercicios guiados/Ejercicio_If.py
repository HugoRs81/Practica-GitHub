import random
var_random = random.randint(1,5)
var_usuario = int(input("introduce un número del 1 al 5: "))
if var_usuario in [1,2,3,4,5]:
    if var_usuario==var_random:
        print("acertaste")
    else:
        print("fallaste")
else:
    print("no has introducido el rango correcto")
