import random
list = ['Banana','Naranja','Uva','Toronja']

#*************************************
ador,Titulo = "","Ahorcado"
print(f"{ador.center(50,'*')}")
print(f"{Titulo.center(50).upper()}")
print(f"{ador.center(50,'*')}")
#*************************************
def Adivina():
    vidas = 3
    while vidas >= 1:
        Palabra = random.choice(list)
        print(f"La palabra que tiene que adivinar tiene: {len(Palabra)} letras\nY empieza con la letra {Palabra[0]}\n")
        print(f"por ahora tiene: {vidas}")
        Usuario = input("Ingrese la palabra: ")
        if Usuario.upper() == Palabra.upper():
            print(f"\nFelicidades le atino la palabra era: {Palabra.title()}")
            break

        else:
            vidas -= 1
            print("\nNo era esa palabra, lo siento menos una vida\n")

        if vidas < 1:
            print("\nPerdiste tus vidas\nFin...")
            break

Adivina()