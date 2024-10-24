print("ce programme permet rendre la monny")
T=[200,100,50,20,10,5,2,1,0.1,0.5,0.1]
montant_payer=float(input("donner le montant de payer: "))
montant_achat=float(input("donner le montant d'achat : "))
if montant_payer > montant_achat:
 montant_reste = montant_payer - montant_achat
 print("le reste du montant est :", montant_reste)
else:
  plus_payer=float(input("donner s'il vous plait plus de payer : "))
if montant_payer == montant_achat:
 print("merci, le montant est tout a fait")








