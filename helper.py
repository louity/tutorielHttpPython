# pour entrer un message dans la console et le stocker dans var
var = raw_input('Entrez votre message : ')

# le caractere \n permet de faire des sauts a la ligne
print('Salut \n Ca va ?')

# la methode split permet de separer un chaine de caractere et stocker les parties dans un tableau
liste1 = 'pomme,poire,peche'
print(liste1)
print(liste1.split(','))

liste2 = 'pomme poire peche'
print(liste2)
print(liste2.split(' '))

liste3 = 'pomme\npoire\npeche'
print(liste3)
print(liste3.split('\n'))

# la methode join fait la transformation inverse
liste = ['pomme', 'poire', 'peche']
separateur1 = ','
print(separateur1.join(liste))
separateur2 = ' '
print(separateur2.join(liste))
separateur3 = '\n'
print(separateur3.join(liste))
