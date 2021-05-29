
# On place l'affichage de chaque chiffre en LCD dans un dictionnaire (en ligne ici)
chiffresLCD = {
    0: [' - ', '| |', '   ', '| |', ' - '],
    1: ['   ', '  |', '   ', '  |', '   '],
    2: [' - ', '  |', ' - ', '|  ', ' - '],
    3: [' - ', '  |', ' - ', '  |', ' - '],
    4: ['   ', '| |', ' - ', '  |', '   '],
    5: [' - ', '|  ', ' - ', '  |', ' - '],
    6: [' - ', '  |', ' - ', '| |', ' - '],
    7: [' - ', '  |', '   ', '  |', '   '],
    8: [' - ', '| |', ' - ', '| |', ' - '],
    9: [' - ', '| |', ' - ', '  |', ' - '],
}


def afficheLCD(nombre):
    # On separe le nombre en liste de chiffres à afficher
    separation = map(int, str(nombre))

    # On fait correspodre ces chiffres avec l'affichage LCD
    transformation = [chiffresLCD[chiffre] for chiffre in separation]

    # On fait une conversion des chiffres à la suite en ligne de caracteres pour
    # l'affichage en LCD

    ''' 
    ##### Ne marche que pour deux elements à la fois #####
    conversion = []
    for i in range(len(separation)-1):
        for j in range(5):
            try:
                if transformation[i+1][j] :
                    print(i)
                    conversion.append(tuple(transformation[i][j] + transformation[i+1][j] ))
            except :
                conversion.append(tuple(transformation[i][j]))
    '''
    # La fonction zip fait une iteration sur tout les premiers elements de chaque elements
    # d'une liste puis tout les seconds elements, etc de façon parallele et resoud le soucis 
    # d'être limité par deux elements à la fois 
    conversion = zip(*transformation)

    # On fait une jointure de tous les elements au sein d'un tuple (ligne pour nous)
    # puis une jointure des tuples entre eux ce qui nous donne des lignes de caracteres que 
    # l'on affiche à l'aide du print. La fin de chaque ligne est delimitée par un espace
    print('\n'.join(''.join(ligne) for ligne in conversion))
    


# On fait une boucle dans laquelle on met un test sur la valeur que l'utilisateur a rentré pour 
# ne pas avoir d'erreur et être sur que l'utilisateur rentre une valeur qui est correcte
blind = True
while blind:
    try:
        # On demande à l'utilisateur de rentrer un chiffre ou un nombre (rond)
        nombre = int(input("Entrez un chiffre ou un nombre à afficher en LCD (il doit être rond) : "))
        blind = False

    # La valeur rentrée par l'utlisateur n'est pas correcte, on lui demande de rentrer une nouvelle valeur
    except ValueError:
        print("L'entrée saisie n'est pas correcte veuillez re-essayer")

# On appelle la fonction qui affiche en LCD la valeur de l'utlisateur en la passant en parametre
afficheLCD(nombre)
