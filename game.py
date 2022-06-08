import random

def carica_parole():
    lista_di_parole = []
    with open('wordlist.txt', 'r') as f:
        for line in f:
            parola = line.rstrip('\n')
            lista_di_parole.append(parola)
    return lista_di_parole

def parola_random(lista_di_parole):
    return random.choice(lista_di_parole)

def visualizza_parola(lista_lettere):
    print(' '.join(lettera for lettera in lista_lettere))

def aggiorna_lettere_indovinate(parola, scelta, lettere_indovinate):
    for i, lettera in enumerate(parola):
        if lettera == scelta:
            lettere_indovinate[i] = lettera
    return lettere_indovinate

def show_player_life():
    life = """
---
"""
    yield life

    life = """
|----
|
|
|
|
---
"""
    yield life
    life = """
|----0
|    |
|    |
|    |
|    |
---
"""
    yield life

    life = """
|----O
|    |
|   /|\
|    |
|    |
---
"""

    yield life

    life = """
|----O
|    |
|   /|\
|    |
|   /|\
---
"""

    yield life
    life = """

|--\
|   \O
|    |
|   /|\
|    |
--- /|\
"""
    yield life


lista_di_parole = carica_parole()
parola_da_indovinare = parola_random(lista_di_parole)
lettere_indovinate = ['_' for lettera in parola_da_indovinare]
vita_giocatore = show_player_life()

visualizza_parola(lettere_indovinate)

while True:
    scelta = input("Inserisci una lettera -> ")
    if scelta in parola_da_indovinare:
        lettere_indovinate = aggiorna_lettere_indovinate(parola_da_indovinare, scelta, lettere_indovinate)
        if parola_da_indovinare == ''.join(lettera for lettera in lettere_indovinate):
            print("Hai vinto, complimenti! La parola è: {0}".format(parola_da_indovinare))
            break
    else:
        try:
            print(next(vita_giocatore))
        except StopIteration:
            print("Hai perso, la parola era: {0}".format(parola_da_indovinare))
            break

    visualizza_parola(lettere_indovinate)