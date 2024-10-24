print("ce programme permet d'affiche un nombre palindrom oui ou non")
nombres=int(input("donner un nombres : "))
inverse = 0
x = nombres
while x >0 :
    inverse = (inverse * 10) + x % 10
    x = x // 10
if inverse == nombres :
    print(f" nombres : {nombres} est palindrome" )
else :
    print(f" nombres : {nombres} n'est pas palindrome")
