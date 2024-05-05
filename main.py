import sys

#Methoden
def even(x):
    x = x / 2
    return x

def odd(x):
    x = (3 * x) + 1
    return x

counter = 0

#x Wert einlesen
while(True):
    try:
        x = float(input("Choose any positive Number: "))
        break
    except ValueError:
        print("!ERROR_1! Choose any positive Number")

if(x <= 0):
    print("!ERROR_2! Choose any positive Number")
    while(True):
        try:
            x = float(input("Choose any positive Number: "))
            break
        except x:
            print("!ERROR_1! Choose any positive Number")

liste = [x]
#Hauptschleife des Programms
while(True):
    if(x % 2 == 0):
        x = even(x)
        liste.append(x)
    else:
        x = odd(x)
        liste.append(x)

    if(x == 4):
        counter = counter + 1
        if(counter == 3):
            break

print(liste[::])
