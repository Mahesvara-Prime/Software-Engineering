
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
        print("Calcule impossible veuillez verifier vos entrer")
    
    return resultats
    
def operator():
    op = ""                   
    while True:
        op = input("Operateur : ")
        if op in ("+", "-", "*", "/"):
            break
        else:
            print("Operateur pas valide veuillez ressayer")
    return op  
    
    
def verifie_calcul(op):
          
    result = 0
    while True:
        try:
            nbr1 = int(input("Entrer votre premier valeur : "))
            nbr2 = int(input("Entrer votre deuxieme valeur : "))
            resul = calcul(nbr1, nbr2, op)
            break
        except ValueError:
            print("Valeur inconnu veuillez entrer des nombre")
        except ZeroDivisionError:
            print("Sorry, pas possible cette diffision par zero")
        except:
            print("Veuillez reprendre s'il vous plait")
    return result

print(''' Veuillez entrer votre operateur:
            1. + pour l'addition
            2. - pour la soustraction
            3. * pour la multiplication
            4. / pour la division''')
            
While True:
    op = operator()
    verifie_calcul(op)
    if continue == "y":
        continue
    else:
        break
    
     
print(f'Votre resultats est : {resul}')