print("ce programme permet d'fficher si la date valid ou non.")
j=int(input("donner le nombre de jours : "))
m=int(input("donner le mois : "))
a=int(input("donner l'annee : "))
T = [ 31, 28, 31, 30, 31, 30, 31,31, 30, 31, 30 , 31  ]
T[1] = 29 if ((a%4 == 0 and a%100!=0 ) or a%400 == 0 ) else 28
if m<=12 and m>=1 :
    print("Date valid") if (j < T[m-1] and a > 0  ) else print("Date invalid !")
else :
    print("Date invalid !")




