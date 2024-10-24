print("ce programme permet d'afficher la table de multiplication .")
a=int(input("donner la valeur a : "))
m = 1

i = 0
while i < 11 :
    m = i * a
    print(f"{a} x {i} = {m}")
    i +=1