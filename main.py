#Version 1.0
#José Miguel Gabela, 2021

import calculadora

#This block asks for the amount of different elements 

rttt = input("Cuantos elementos diferentes: ")

try:
    rttt = int(rttt)
except:
    rttt = input("Cuantos elementos diferentes: ")

#This block asks the amount of atoms of the elements

trtt = input("Cuantos atomos hay en total? ")

try:
    trtt = int(trtt)
except:
    trtt = input("Cuantos atomos hay en total? ")

#These blocks returns the moles of the elements given by the user

if rttt == 1:
    a = input("Ingresa el elemento: ")
    calculadora.n(a)
    print("La masa de litio es", calculadora.n.rr)
    rf = calculadora.n.rr * trtt
    print(rf)

if rttt == 2:
    a = input("Ingresa elemento 1: ")
    b = input("Ingresa elemento 2: ")
    calculadora.n1(a, b)