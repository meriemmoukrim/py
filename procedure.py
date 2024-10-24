def Menu():
    print("1 - Remplir le Tableau.")
    print("2 - Afficher le Tableau.")
    print("3 - Rechercher une valeur.")
    print("4 - Remplacer une valeur.")
    print("5 - Trier le Tableau.")
    print("6 - Vider le Tableau.")
    print("0 - Quitter.")

# Remplissage du Tableau
def Remplire():
    T = []
    Case_Tableau = int(input("Entrez case de tableau : "))
    for i in range(Case_Tableau) :
        a = int(input(f"Entrez la valeur {i + 1} : "))
        T.append(a)
    return T

# Affichage du Tableau
def AfficherT(T):
    print(T)

# Rechere d'une valeur s'il existe ou non
def Recherche(T):
    valeur_Recherche = int(input("donner la valeur de recherche : "))
    trouve= False
    for i in range(len(T)):
        if T[i] == valeur_Recherche:
            print(f"La valeur recherchée est {valeur_Recherche} à la position {i + 1}")
            trouve = True
    if not trouve:
        print(f"La valeur recherche {valeur_Recherche} n'existe pas dans le tableau.")

# Remplacer une valeur par une autre valeur
def Remplacer(T):
    valeur_Recherche = int(input("donner la valeur de recherche : "))
    valeur_Remplacer = int(input("donner la valeur de  remplacer : "))
    trouve = False
    for i in range(len(T)):
        if T[i] == valeur_Recherche:
            print(f"La valeur recherche est {valeur_Recherche} à la position {i + 1}")
            T[i] = valeur_Remplacer
            trouve = True
    if not trouve :
            print(f"La valeur recherche {valeur_Recherche} n'existe pas dans le tableau.")
    print (T)

#le trie de tableau
def Trie(T):
        for i in range(len(T) - 1):
            for k in range ( i + 1 , len(T)) :
                if T[i] > T[k] :
                    T[i] , T[k] = T[k] , T[i]
        print("Le tableau est trie")

# Vide le tableau
def Vide(T):
    T.clear()
    print("Le tableau est vide.")
    print(T)
choix = 10
T = []  # Initialisation du tableau
while choix != 0:
    Menu()
    choix = int(input("Entrez un choix : "))
    match choix:
        case 1:
            T = Remplire()
        case 2:
            AfficherT(T)
        case 3:
            Recherche(T)
        case 4:
            Remplacer(T)
        case 5:
            Trie(T)
        case 6:
            Vide(T)
        case 0:
            print("le Programme est terminer.")
        case _:
            print("le Choix est invalide")