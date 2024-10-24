print("ce programme permet d'affiche les mois")
mois=int(input("donner le mois : "))
T=["janvier","février","mars","april","mai","juine","juillet","septembre","aout","october","november","decembre"]
if 0 < mois <= 12:
    print(f"le mois est : {T[mois-1]} ")
else :
     print("ERREUR!!!!")