solde = 100
def ajoute_intérêt(solde,taux):
    solde += solde * taux/100
    
for année in range(4):
    ajoute_intérêt(solde,5)
    print('Solde après l\'année {} : {:.2f} €'.format(année+1,solde))
