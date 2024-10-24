print("ce programme permet d'affiche la valeur choisi dans tableau")
def tableau(T):
    valeur_choisie = None
    while  valeur_choisie not in T :
        valeur_choisie = int(input("donner la valeur choisie : "))
        if valeur_choisie not in T:
            print("introuvable,recommencer.")
    return valeur_choisie

T = [111,20,3,49,58,16,9,5]
valeur = tableau(T)
print(f"La valeur est : {valeur}")