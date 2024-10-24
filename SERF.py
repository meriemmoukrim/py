print("ce programme permet rendre la monny")
T=[200,100,50,20,10,5,2,1,0.5,0.1]
n=int(input("combien d'article avez-vous ? "))
somme = 0
for i in range(n+1):
    prix=float(input("donner le prix : "))
    quantité=float(input("donner la quantité : "))
    somme = prix * quantité + somme
print(f"montant payer est {somme} ")
montant_achat=float(input("donner le montant d'achat : "))
reste = montant_achat - somme
rendu = {}
print(" le reste de montant est :", reste)
for i in T :
    if reste >= i :
        nombre = reste // i
        rendu[i] = (nombre)
        reste = reste - nombre * i
print ("rendu de monnaie :")
for i , nombre in rendu.items() :
    if nombre > 0:
        if i >= 5 :
            print (f"{nombre} billets de {i} DH ")
        else :
            print(f"{nombre} billets de {i} DH ")