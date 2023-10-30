import random
chances = 4
nombre_secret = random.randint(1,10)

def guessnumber():
    nombre_secret


print("Salam Aleykoum, bienvenu dans mon jeu, tia 4 chances le sang")

while chances > 0:
    try:
        player = int(input("Entrez votre valeur :"))
    except ValueError:
        print("Met une valeur valide")
        continue

    if player < 1 or player > 10:
        print("Le nombre doit être entre 1 et 10")
        continue

    if player == nombre_secret: 
        print("Félicitations tia trouver le bon nombre : ", nombre_secret)
        break
    else:
        chances -= 1
        if chances > 0:
            print(f"Ce n'est pas le bon numéro, il te reste {chances} essais")
        else:
            print(f"Tu n'as plus d'essais le sang !, le nombre était {nombre_secret}")
            break

if __name__ == "__main__":
    guessnumber()