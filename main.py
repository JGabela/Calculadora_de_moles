#Version 2.22
#José Miguel Gabela, 2021

import calculadora
import masa_mol_dict

print("")
print("Calculadora de Moles")
print("Version 2.22")
print("")

print("Ingresa el compuesto o el elemento quimico")
trrr = input("")
raw = trrr

print("")

#this block separate the letters of the list and form the elements of the compund 

trrr = list(trrr)

for a in trrr:
    b = a.isupper()
    if b is False:
        try:
            a = int(a)
        except:
            if type(a) is str:
                c = trrr.index(a)
                d = c - 1
                a1 = trrr[c]
                a2 = trrr[d]
                p = a2 + a1
                trrr.pop(c)
                trrr.pop(d)
                trrr.insert(d, p)


#This block enables to use sub index bigger than 9
#
#for l in trrr:
#    if type(l) is int:
#        l = str(l)
#        k = trrr.index(l)
#        k = k + 1
#        if type(k) is int:
#            j = trrr[k]
#            j = str(j)
#            ar = l + j
#            ar = int(ar)
#            trrr.pop(l)
#            trrr.pop(j)
#            k = k - 1
#            trrr.insert(k, ar)

#this block determines which element has a subindex of 1 (to be replace)

ter = len(trrr)

ter = ter - 1
tir = trrr[ter]

try:
    trrr[ter] = int(tir)
except:
    ter = ter + 1
    trrr.insert(ter, 1)
    ter = ter - 1

#this block extracts each element from the compound

n = True

while n == True:

    try:
        a = trrr[0]
    except:
        a = False
        b = False
        c = False
        d = False
        e = False
        break

    try:
        b = trrr[2]
    except:
        b = False
        c = False
        d = False
        e = False
        break

    try:
        c = trrr[4]
    except:
        c = False
        d = False
        e = False
        break

    try:
        d = trrr[6]
    except:
        d = False
        e = False
        break

    try:
        e = trrr[8]
    except:
        e = False
        break

    n = False

#this block extract the subindex of each element

t = True

while t == True:

    try:
        an = int(trrr[1])
    except:
        an = False
        bn = False
        cn = False
        dn = False
        en = False
        break

    try:
        bn = int(trrr[3])
    except:
        bn = False
        cn = False
        dn = False
        en = False
        break

    try:
        cn = int(trrr[5])
    except:
        cn = False
        dn = False
        en = False
        break

    try:
        dn = int(trrr[7])
    except:
        dn = False
        en = False
        break

    try:
        en = int(trrr[9])
    except:
        en = False
        break

    t = False



while True:
    if a != False:
        calculadora.n(a)
        va = calculadora.n.tr

        if b != False:
            calculadora.n(b)
            vb = calculadora.n.tr

            if c != False:
                calculadora.n(c)
                vc = calculadora.n.tr

                if d != False:
                    calculadora.n(d)
                    vd = calculadora.n.tr

                    if e != False:
                        calculadora.n(e)
                        ve = calculadora.n.tr
                        ven = (va * an) + (vb * bn) + (vc * cn) + (vd * dn) + (ve * en)
                        print('Masa Molar del compuesto', ven, 'g/mol')
                        print('')
                        print("Cantidad de atomos de:", a)
                        aol = masa_mol_dict.mol * an
                        print(a, ":", aol, "e+23")
                        print('')
                        print("Cantidad de atomos de:", b)
                        bol = masa_mol_dict.mol * bn
                        print(b, ":", bol, "e+23")
                        print('')
                        print("Cantidad de atomos de:", c)
                        col = masa_mol_dict.mol * cn
                        print(c, ":", col, "e+23")
                        print('')
                        print("Cantidad de atomos de:", d)
                        dol = masa_mol_dict.mol * dn
                        print(d, ":", dol, "e+23")
                        print('')
                        print("Cantidad de atomos de:", e)
                        eol = masa_mol_dict.mol * en
                        print(e, ":", eol, "e+23")
                        print('')
                        print(
                            "Quieres la cantidad de moles en cierta cantidad de gramos?",
                            "O la cantidad de gramos en cierta cantidad de moles?"
                            )
                        ida = input('')
                        if ida == 'done':
                            exit()
                        if ida == "moles":
                            mas = input("Ingresa la cantidad de gramos que hay: ")
                            nummol = float(mas) / ven
                            print("Hay", nummol, "moles en", mas, "gramos de", raw)

                        if ida == "gramos":
                            soup = input('Ingresa la cantidad de moles que hay: ')
                            nugr = ven * float(soup)
                            print("Hay", nugr, "gramos en", soup, "moles de", raw)
                        break

                    vdn = (va * an) + (vb * bn) + (vc * cn) + (vd * dn)
                    print('Masa Molar del compuesto', vdn, 'g/mol')
                    print('')
                    print("Cantidad de atomos de:", a)
                    aol = masa_mol_dict.mol * an
                    print(a, ":", aol, "e+23")
                    print('')
                    print("Cantidad de atomos de:", b)
                    bol =  masa_mol_dict.mol * bn
                    print(b, ":", bol, "e+23")
                    print('')
                    print("Cantidad de atomos de:", c)
                    col = masa_mol_dict.mol * cn
                    print(c, ":", col, "e+23")
                    print('')
                    print("Cantidad de atomos de:", d)
                    dol = masa_mol_dict.mol * dn
                    print(d, ":", dol, "e+23")
                    print('')
                    print(
                        "Quieres la cantidad de moles en cierta cantidad de gramos?",
                        "O la cantidad de gramos en cierta cantidad de moles?"
                        )
                    ida = input('')
                    if ida == 'done':
                        exit()
                    if ida == "moles":
                        mas = input("Ingresa la cantidad de gramos que hay: ")
                        nummol = float(mas) / vdn
                        print("Hay", nummol, "moles en", mas, "gramos de", raw)

                    if ida == "gramos":
                        soup = input('Ingresa la cantidad de moles que hay: ')
                        nugr = vdn * float(soup)
                        print("Hay", nugr, "gramos en", soup, "moles de", raw)
                    break

                vcn = (va * an) + (vb * bn) + (vc * cn)
                print('Masa Molar del compuesto', vcn, 'g/mol')
                print('')
                print("Cantidad de atomos de:", a)
                aol = masa_mol_dict.mol * an
                print(a, ":", aol, "e+23")
                print('')
                print("Cantidad de atomos de:", b)
                bol =  masa_mol_dict.mol * bn
                print(b, ":", bol, "e+23")
                print('')
                print("Cantidad de atomos de:", c)
                col = masa_mol_dict.mol * cn
                print(c, ":", col, "e+23")
                print('')
                print(
                    "Quieres la cantidad de moles en cierta cantidad de gramos?",
                    "O la cantidad de gramos en cierta cantidad de moles?"
                    )
                ida = input('')
                if ida == 'done':
                      exit()
                if ida == "moles":
                    mas = input("Ingresa la cantidad de gramos que hay: ")
                    nummol = float(mas) / vcn
                    print("Hay", nummol, "moles en", mas, "gramos de", raw)

                if ida == "gramos":
                    soup = input('Ingresa la cantidad de moles que hay: ')
                    nugr = vcn * float(soup)
                    print("Hay", nugr, "gramos en", soup, "moles de", raw)
                break

            vbn = (va * an) + (vb * bn)
            print('Masa Molar del compuesto', vbn, 'g/mol')
            print('')
            print("Cantidad de atomos de:", a)
            aol = masa_mol_dict.mol * an
            print(a, ":", aol, "e+23")
            print('')
            print("Cantidad de atomos de:", b)
            bol =  masa_mol_dict.mol * bn
            print(b, ":",bol, "e+23")
            print('')
            print(
                "Quieres la cantidad de moles en cierta cantidad de gramos?",
                "O la cantidad de gramos en cierta cantidad de moles?"
                )
            ida = input('')
            if ida == "moles":
                mas = input("Ingresa la cantidad de gramos que hay: ")
                nummol = float(mas) / vbn
                print("Hay", nummol, "moles en", mas, "gramos de", raw)

            if ida == "gramos":
                soup = input('Ingresa la cantidad de moles que hay: ')
                nugr = vbn * float(soup)
                print("Hay", nugr, "gramos en", soup, "moles de", raw)
            break

        van = va * an
        print('Masa Molar del compuesto', van, 'g/mol')
        print('')
        print("Cantidad de atomos de:", a)
        print(a, ":", masa_mol_dict.mol * an, "e+23")
        print('')
        print(
            "Quieres la cantidad de moles en cierta cantidad de gramos?",
            "O la cantidad de gramos en cierta cantidad de moles?"
            )
        ida = input('')
        if ida == 'done':
            exit()
        if ida == "moles":
            mas = input("Ingresa la cantidad de gramos que hay: ")
            nummol = float(mas) / van
            print("Hay", nummol, "moles en", mas, "gramos de", raw)

        if ida == "gramos":
            soup = input('Ingresa la cantidad de moles que hay: ')
            nugr = van * float(soup)
            print("Hay", nugr, "gramos en", soup, "moles de", raw)
        break
