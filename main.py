#Version 2.22
#José Miguel Gabela, 2021

import calculadora
import masa_mol_dict

print("")
print("Calculadora de Moles")
print("Version 2.22")
print("")

print("Ingresa el compuesto o el elemento quimico")
Compuesto = input("")
raw = Compuesto

print("")

#this block separate the letters of the list and form the elements of the compund 

Compuesto = list(Compuesto)

for a in Compuesto:
    b = a.isupper()
    if b is False:
        try:
            a = int(a)
        except:
            if type(a) is str:
                c = Compuesto.index(a)
                d = c - 1
                a1 = Compuesto[c]
                a2 = Compuesto[d]
                p = a2 + a1
                Compuesto.pop(c)
                Compuesto.pop(d)
                Compuesto.insert(d, p)

#this block determines which element has a subindex of 1 (to be replace)

CompuestoLength = len(Compuesto)

CompuestoLength = CompuestoLength - 1
tir = Compuesto[CompuestoLength]

try:
    Compuesto[CompuestoLength] = int(tir)
except:
    CompuestoLength = CompuestoLength + 1
    Compuesto.insert(CompuestoLength, 1)
    CompuestoLength = CompuestoLength - 1

#this block of code turns all numbers into integers

for a in Compuesto:
    try:
        reemplazo = int(a)
        indexA = Compuesto.index(a)
        Compuesto.pop(indexA)
        Compuesto.insert(indexA, reemplazo)
    except:
        continue

#this block enables subindex bigger than 9

for a in Compuesto:
    if type(a) is int:
        b = Compuesto.index(a)
        c = b + 1
        try:
            d = Compuesto[c]
            e = Compuesto.index(d)
            if type(d) is int:
                num1 = str(a)
                num2 = str(d)
                reemplazo = num1 + num2
                del Compuesto[e]
                del Compuesto[b]
                Compuesto.insert(b, reemplazo)
            else:
                continue
        except:
            break
    else:
        continue

#this block extracts each element from the compound

n = True

while n == True:

    try:
        a = Compuesto[0]
    except:
        a = False
        b = False
        c = False
        d = False
        e = False
        break

    try:
        b = Compuesto[2]
    except:
        b = False
        c = False
        d = False
        e = False
        break

    try:
        c = Compuesto[4]
    except:
        c = False
        d = False
        e = False
        break

    try:
        d = Compuesto[6]
    except:
        d = False
        e = False
        break

    try:
        e = Compuesto[8]
    except:
        e = False
        break

    n = False

#this block extract the subindex of each element

t = True

while t == True:

    try:
        an = int(Compuesto[1])
    except:
        an = False
        bn = False
        cn = False
        dn = False
        en = False
        break

    try:
        bn = int(Compuesto[3])
    except:
        bn = False
        cn = False
        dn = False
        en = False
        break

    try:
        cn = int(Compuesto[5])
    except:
        cn = False
        dn = False
        en = False
        break

    try:
        dn = int(Compuesto[7])
    except:
        dn = False
        en = False
        break

    try:
        en = int(Compuesto[9])
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
                        print('Masa Molar de', raw, ':', ven, 'g/mol')
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
                    print('Masa Molar de', raw, ':', vdn, 'g/mol')
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
                print('Masa Molar de', raw, ':', vcn, 'g/mol')
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
            print('Masa Molar de', raw, ':', vbn, 'g/mol')
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
        print('Masa Molar de', raw, ':', van, 'g/mol')
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
