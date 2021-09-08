#Version 1.1
#José Miguel Gabela, 2021

import calculadora

print("")
print("Calculadora de Moles")
print("Version 1.1")
print("")

print("Ingresa el compuesto o el elemento quimico")
print('(cada elemento y subindice tiene que ser separado por "#")')
#trrr = input("")
trrr = "O#2"

print("")

#this block of code gets the number of elements in the compound
trrt = trrr.split('#')
ate = len(trrt)
ate = ate - 1

#this block extracts each element from the compound 

n = True

while n == True:

    try:
        a = trrt[0]
    except:
        a = False
        b = False
        c = False
        d = False
        e = False
        break

    try:
        b = trrt[2]
    except:
        b = False
        c = False
        d = False
        e = False
        break

    try:
        c = trrt[4]
    except:
        c = False
        d = False
        e = False
        break

    try:
        d = trrt[6]
    except:
        d = False
        e = False
        break

    try:
        e = trrt[8]
    except:
        e = False
        break

    n = False

#this block extract the subindex of each element

t = True

while t == True:

    try:
        an = int(trrt[1])
    except:
        an = False
        bn = False
        cn = False
        dn = False
        en = False
        break

    try:
        bn = int(trrt[3])
    except:
        bn = False
        cn = False
        dn = False
        en = False
        break

    try:
        cn = int(trrt[5])
    except:
        cn = False
        dn = False
        en = False
        break

    try:
        dn = int(trrt[7])
    except:
        dn = False
        en = False
        break

    try:
        en = int(trrt[9])
    except:
        en = False
        break

    t = False

if a != False:
    calculadora.n(a)
    va = calculadora.n.tr
    van = va * an
    print('masa molar del compuesto', van, 'u')

if b != False:
    calculadora.n(b)
    vb = calculadora.n.tr
    vbn = (va * an) + (vb * bn)

if c != False:
    calculadora.n(c)
    vc = calculadora.n.tr

if d != False:
    calculadora.n(d)
    vd = calculadora.n.tr

if e != False:
    calculadora.n(e)
    ve = calculadora.n.tr
