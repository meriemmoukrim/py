print("ce programme permet d'affiche la valeur tempoeraire")
second=int(input("donner second : "))
heurs = second // 3600
reste = second % 3600
minute = reste// 60
second = reste % 60
print(f"{heurs}:{minute}:{second}")




