var1 = 12 
var2 = 17.9
var3 = 'SdE2'

x =type(var1)
y =type(var2)
z =type(var3)

print(x ,var1)
print(y,var2)
print(z,var3)


nombre = input('Écris un nombre entier positif : ')

nombre = int(nombre)



i = 2

while i < nombre and nombre % i != 0 :

    i = i + 1

if i == nombre :

    est_premier = True

else :

    est_premier = False


if est_premier :

    print('Le nombre', nombre, 'est premier ')

else :

    print('Ce n\'est pas un nombre premier.')
    
    

fruits = ["banane","pomme","orange","peche","poire"]

def tri(liste):
    if not liste:
        return []
    return (tri([x for x in liste[1:] if x <  liste[0]])
            + [liste[0]] +
            tri([x for x in liste[1:] if x >= liste[0]]))


print(tri(fruits))
  

    