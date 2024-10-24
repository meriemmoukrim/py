def Date_valide(a,m,j):
    T = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    T[1] = 29 if ((a % 4 == 0 and a% 100 != 0) or a % 400 == 0) else 28
    if m <= 12 and m >= 1 and j >=1 and j<=T[m-1]:
        return True
    else:
        return False

print("la date est valide oui ou non ")
annee=int(input("donner l'annee : "))
mois=int(input("donner le mois : "))
jours=int(input("donner le jours : "))
if Date_valide(annee,mois,jours)==True :
    print("date valide")
else:
    print("date invalide")
