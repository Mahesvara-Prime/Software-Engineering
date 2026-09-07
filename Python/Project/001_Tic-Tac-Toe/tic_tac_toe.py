from random import randrange

def display_board(plateau) :
    # La fonction accepte un paramètre contenant l'état actuel du plateau
    # et l'affiche sur la console.
    bordure = "+----+-----+-----+"
    ligne = "|    |     |     |"
    print(bordure)
    print(ligne)
    print("|  " + str(plateau[0][0]) +" |  " + str(plateau[0][1])+ "  |  " + str(plateau[0][2])+"  |")
    print(ligne)
    print(bordure)
    print(ligne)
    print("|  " + str(plateau[1][0]) +" |  " + str(plateau[1][1])+ "  |  " + str(plateau[1][2])+"  |")
    print(ligne)
    print(bordure)
    print(ligne)
    print("|  " + str(plateau[2][0]) +" |  " + str(plateau[2][1])+ "  |  " + str(plateau[2][2])+"  |")
    print(ligne)
    print(bordure)


def enter_move(plateau) :
    # La fonction accepte l'état actuel du plateau, demande à l'utilisateur quel coup il souhaite jouer, 
    # vérifie la saisie et met à jour le plateau en fonction de la décision de l'utilisateur.
    while True:
        saisie = input("Enter your move : ")
        
        #Vérification 1 : est-ce un nombre entier ?
        if not saisie.isdigit():
            print("Entre un nombre entier !")
            continue
        
        numero = int(saisie)
        
        # Vérification 2 (à toi) : numero est-il entre 1 et 9 ?
        if 1 <= numero <= 9:
            ligne = (numero - 1) // 3
            colonne = (numero - 1) % 3
        else:
            print("Veuillez entrer un nombre compris entre 1 et 9")
            continue
        
        # Vérification 3 (à toi) : la case (ligne, colonne) est-elle libre ?
        if (ligne,colonne) in make_list_of_free_fields(plateau):
            plateau[ligne][colonne] = "O"
            break
        else:
            print("Place deja occupé")
            continue
        
        
    

def make_list_of_free_fields(board):
    # La fonction parcourt le plateau et construit une liste de toutes les cases libres ; 
    # la liste est composée de tuples, chaque tuple étant une paire de numéros de ligne et de colonne.
    libres = []
    
    for ligne in range(3):
        for colonne in range(3):
            if board[ligne][colonne] != 'X' and board[ligne][colonne] != 'O':
                libres.append((ligne,colonne))
                
    return libres       

def victory_for(board, sign):
    # La fonction analyse l'état du plateau afin de vérifier si 
    # le joueur utilisant les « O » ou les « X » a gagné la partie
    # Lignes horizontales
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True

    # Colonnes verticales
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    # colonne 1  → (0,1), (1,1), (2,1)
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    # colonne 2  → (0,2), (1,2), (2,2)
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True

    # Diagonales
    # Diagonale descendante → (0,0), (1,1), (2,2)
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    # Diagonale montante    → (0,2), (1,1), (2,0)
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    # Si aucune combinaison n'a marché :
    # renvoyer False
    return False
    

def draw_move(board):
    # La fonction effectue le coup de l'ordinateur et met à jour le plateau
    libres = make_list_of_free_fields(board)
    # 1. hasard = un index aléatoire avec randrange
    hasard = randrange(len(libres))
    # 2. ligne, colonne = le tuple choisi dans libres
    choix = libres[hasard]      
    ligne, colonne = choix 
    # 3. placer 'X' dans plateau[ligne][colonne]
    board[ligne][colonne] = "X"



while True:
    plateau = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
    ]
    
    while True:
        # Afficher le plateau
        display_board(plateau)
        # Coup de l'utilisateur
        enter_move(plateau)
        # Si victory_for(plateau, 'O') → print("You won!") puis break
        if victory_for(plateau, 'O'):
            print("YOU WIN!")
            break
        # Si plus de case libre → print("Draw!") puis break
        if not make_list_of_free_fields(plateau):
            print("Draw!")
            break
        # Coup de l'ordinateur
        draw_move(plateau)
        # (à toi) si victory_for(plateau, 'X') → print("You lost!") puis break
        if victory_for(plateau, 'X'):
            print("YOU LOST!")
            break
        # Si plus de case libre → print("Draw!") puis break
        if not make_list_of_free_fields(plateau):
            print("Draw!")
            break
        
    # demander : 
    Replay = input("Do you want to play again? (yes/no): ")
    # Si la réponse est "no" → break
    if Replay == "no":
        break
    