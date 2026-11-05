respuesta = input("introduce una letra: ")
if respuesta.isalpha()==True:
    if respuesta.isupper()==True:
        print("es mayúscula")
    else:
        print("es minúscula")
else:
    print("el valor introducido no es una letra")