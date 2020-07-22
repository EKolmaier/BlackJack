# BlackJack
import time
import random

def countdown(t):
    while t > 0:
        print(str(t))
        t -= 1
        time.sleep(1)

def generar_mazo():
    mazo = []
    j = 1
    while j <= 4:
        i = 1
        while i <= 10:
            z=1
            if i == 10:
                while z < 3:
                    mazo.append(i)
                    z = z+1
            mazo.append(i)
            i = i + 1
        j=j+1
    random.shuffle(mazo)
    return mazo

def dar_cartas(mazo):
    Jugador =[mazo.pop(0),mazo.pop(0),]
    Banca = [mazo.pop(0)]
    return Jugador, Banca


def dar_carta_jugador(mazo,persona):
    res = True
    while True:
        inp = str(input("Otra carta? (C) / Plantarse (P)"))
        if inp in {'C','c'}:
            persona.append(mazo.pop(0))
            if sum(persona) <= 21:
                print("Tus cartas son: " + str(persona) + " Total: " + str(sum(persona)))
            else:
                print("Tus cartas son: " + str(persona) + " Total: " + str(sum(persona)))
                print("Te pasaste")
                res = False
                return res
        elif inp in {'P','p'}:
            print ("Te plantaste con: " + str(sum(persona)))
            time.sleep(1)
            break
        else:
            print("Debes elegir C (otra carta) o P (plantarse)") 


def dar_carta_banca(mazo,persona):
    while True:
            persona.append(mazo.pop(0))
            if sum(persona) < 21:
                print("Las cartas de la banca son: " + str(persona) + " Total: " + str(sum(persona)))
                time.sleep(1)
            elif sum(persona) == 21:
                print("Las cartas de la banca son: " + str(persona) + " Total: " + str(sum(persona)))
                time.sleep(1)
                print("Gana la banca con 21")
                break
            else:
                print("Las cartas de la banca son: " + str(persona) + " Total: " + str(sum(persona)))
                time.sleep(1)
                print("La banca se paso, GANASTE!")
                break


# Bienvenida: inicio #
print("Bienvenido a BlackJack")
time.sleep(1)
print("")
print("")
print("Mezclando cartas... ")
time.sleep(1)
countdown(3)
# Bienvenida: fin #



# Cartas iniciales: inicio #
mazo = generar_mazo()

Jugador,Banca = dar_cartas(mazo)

print("Tus cartas son: " + str(Jugador) + " Total: " + str(sum(Jugador)))
print("La Banca tiene: " + str(Banca) + " Total: " + str(sum(Banca)))
# Cartas iniciales: fin #



# Jugador pide cartas: inicio
res = dar_carta_jugador(mazo,Jugador)
if res == 0:
    exit()
# Jugador pide cartas: fin



# Banca pide cartas: inicio
print("Turno de la banca...")
dar_carta_banca(mazo,Banca)
# Bnaca pide cartas: fin





# Fin
input('Press ENTER to exit')

