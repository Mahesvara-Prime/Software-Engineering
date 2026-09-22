
def operator(nbr1,nbr2,op):
    resultats = 0
    if op == "+":
        resultats = nbr1 + nbr2
    if op == "-":
        resultats = nbr1 - nbr2
    if op == "*":
        resultats = nbr1 * nbr2
    if op == "/":
        resultats = nbr1 / nbr2
    
    return resultats
    
def verifie_operator():
    op = ""
    print(''' Veuillez entrer votre operateur:
            1. + pour l'addition
            2. - pour la soustraction
            3. * pour la multiplication
            4. / pour la division''')
                   
    while True:
        op = input("Operateur : ")
        if op in ("+", "-", "*", "/"):
            break
        else:
            print("Operateur pas valide veuillez ressayer")
    return op  
    
    
def calcul():
          
    result = 0
    while True:
        try:
            nbr1 = int(input("Entrer votre premier valeur : "))
            nbr2 = int(input("Entrer votre deuxieme valeur : "))
            resul = operator(nbr1, nbr2, op)
            break
        except ValueError:
            print("Valeur inconnu veuillez entrer des nombre")
        except ZeroDivisionError:
            print("Sorry, pas possible cette diffision par zero")
        except:
            print("Veuillez reprendre s'il vous plait")


While True:
    Verife_operator()
     
print(f'Votre resultats est : {resul}')