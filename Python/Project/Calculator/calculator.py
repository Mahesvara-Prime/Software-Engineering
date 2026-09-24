
def calcul(nbr1,nbr2,op):
    resultats = 0
    if op == "+":
        resultats = nbr1 + nbr2
    elif op == "-":
        resultats = nbr1 - nbr2
    elif op == "*":
        resultats = nbr1 * nbr2
    elif op == "/":
        resultats = nbr1 / nbr2
    else:
        return None
    
    return resultats
    
def operateur():
    op = ""                   
    while True:
        op = input("Operateur : ")
        if op in ("+", "-", "*", "/"):
            break
        else:
            print("Operateur pas valide veuillez ressayer")
    return op  
    
    
def verifie_calcul(op):      
    resul = 0
    while True:
        try:
            nbr1 = float(input("Entrer votre premier valeur : "))
            nbr2 = float(input("Entrer votre deuxieme valeur : "))
            resul = calcul(nbr1, nbr2, "^")
            if resul == None:
                print("L'opérateur n'est pas correcte veuillez vérifier")
                continue
            else:
                break
        except ValueError:
            print("Valeur inconnu veuillez entrer des nombre")
        except ZeroDivisionError:
            print("Sorry, pas possible cette diffision par zero")
        except:
            print("Veuillez reprendre s'il vous plait")
    return resul


print(''' Veuillez entrer votre operateur:
            1. + pour l'addition
            2. - pour la soustraction
            3. * pour la multiplication
            4. / pour la division''')
     
history = []
    
while True:
    op = operateur()
    result = verifie_calcul(op)
    print(f'Votre resultats est : {result}')
    history.append(result)
    play = input("Voulez-vous continuer y/n : ")
    if play == "y":
        continue
    else:
        break
    
     
print(f'Historique des resultats : {history}')