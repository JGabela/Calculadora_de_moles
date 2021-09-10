#Version 1.1
#José Miguel Gabela, 2021

import calculadora
import masa_mol_dict

print("")
print("Calculadora de Moles")
print("Version 1.1")
print("")

print("Ingresa el compuesto o el elemento quimico")
print('(cada elemento y subindice tiene que ser separado por "#")')
#trrr = input("")
trrr = "Na#1"

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
                        print('Masa Molar del compuesto', ven, 'g/mol-1')
                        print('')
                        print("Cantidad de atomos/molecualas de:", a)
                        aol = masa_mol_dict.mol * an
                        print(a, ":", aol, "e+23")
                        print('')
                        print("Cantidad de atomos/moleculas de:", b)
                        bol = masa_mol_dict.mol * bn
                        print(b, ":", bol, "e+23")
                        print('')
                        print("Cantidad de atomos/moleculas de:", c)
                        col = masa_mol_dict.mol * cn
                        print(c, ":", col, "e+23")
                        print('')
                        print("Cantidad de atomos/moleculas de:", d)
                        dol = masa_mol_dict.mol * dn
                        print(d, ":", dol, "e+23")
                        print('')
                        print("Cantidad de atomos/moleculas de:", e)
                        eol = masa_mol_dict.mol * en
                        print(e, ":", eol, "e+23")
                        print('')
                        break

                    vdn = (va * an) + (vb * bn) + (vc * cn) + (vd * dn)
                    print('Masa Molar del compuesto', vdn, 'g/mol-1')
                    print('')
                    print("Cantidad de atomos/moleculas de:", a)
                    aol = masa_mol_dict.mol * an
                    print(a, ":", aol, "e+23")
                    print('')
                    print("Cantidad de atomos/moleculas de:", b)
                    bol =  masa_mol_dict.mol * bn
                    print(b, ":", bol, "e+23")
                    print('')
                    print("Cantidad de atomos/moleculas de:", c)
                    col = masa_mol_dict.mol * cn
                    print(c, ":", col, "e+23")
                    print('')
                    print("Cantidad de atomos/moleculas de:", d)
                    dol = masa_mol_dict.mol * dn
                    print(d, ":", dol, "e+23")
                    print('')
                    break

                vcn = (va * an) + (vb * bn) + (vc * cn)
                print('Masa Molar del compuesto', vcn, 'g/mol-1')
                print('')
                print("Cantidad de atomos/moleculas de:", a)
                aol = masa_mol_dict.mol * an
                print(a, ":", aol, "e+23")
                print('')
                print("Cantidad de atomos/moleculas de:", b)
                bol =  masa_mol_dict.mol * bn
                print(b, ":", bol, "e+23")
                print('')
                print("Cantidad de atomos/moleculas de:", c)
                col = masa_mol_dict.mol * cn
                print(c, ":", col, "e+23")
                print('')
                break

            vbn = (va * an) + (vb * bn)
            print('Masa Molar del compuesto', vbn, 'g/mol-1')
            print('')
            print("Cantidad de atomos/moleculas de:", a)
            aol = masa_mol_dict.mol * an
            print(a, ":", aol, "e+23")
            print('')
            print("Cantidad de atomos/moleculas de:", b)
            bol =  masa_mol_dict.mol * bn
            print(b, ":",bol, "e+23")
            print('')
            break

        van = va * an
        print('Masa Molar del compuesto', van, 'g/mol-1')
        print('')
        print("Cantidad de atomos/moleculas de:", a)
        print(a, ":", masa_mol_dict.mol * an, "e+23")
        print('')
        print("Quieres la cantidad de moles en cierta cantidad de gramos, o la cantidad de gramos en cierta cantidad de moles?")
        ida = input('')
        if ida == "moles":
            mas = input("Ingresa la cantidad de gramos que hay: ")
            nummol = int(mas) / van
            print("Hay", nummol, "moles en", mas, "gramos de", trrr)

        if ida == "gramos":
            soup = input('Ingresa la cantidad de moles que hay: ')
            nugr = van * int(soup)
            print("Hay", nugr, "gramos en", soup, "moles de", trrr)

        break
