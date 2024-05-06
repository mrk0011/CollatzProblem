import sys

#Methoden
def even(x):
    x = x / 2
    return x

def odd(x):
    x = (3 * x) + 1
    return x

def inputRead():
    x = 0
    while(True):
        try:
            x = float(input("Choose any positive Number: "))
            if(x > 0):
                break
            else:
                print("!ERROR_2! Choose any positive Number")
        except ValueError:
            print("!ERROR_1! Choose any positive Number")
    return x

'''
def listCreator(y: int) -> list[list]:
    listen: list[list] = []
    for i in range(y):
        listen.append([])
    return listen
'''

#Variablen
cnt1 = 0
cnt2 = 0
rangeList = (int(input("Choose how many different numbers you want to insert: ")))

listen: list[list] = []
for i in range(rangeList):
    listen.append([])

#Hauptschleife des Programms
while(cnt1 < rangeList):
    x = inputRead()

    while(True):
        if(x % 2 == 0):
            x = even(x)
            listen[cnt1].append(x)
        else:
            x = odd(x)
            listen[cnt1].append(x)

        if(x == 4):
            cnt2 = cnt2 + 1
            if(cnt2 == 3):
                cnt2 = 0
                print(listen[cnt1][::])
                cnt1 = cnt1 + 1
                break