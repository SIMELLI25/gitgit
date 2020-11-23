input("ES 1")

c1 = input("nome primo candidato: ")
c2 = input("nome secondo candidato :")
nvoti = int(input("Quanti voti ci sono? "))
voti = 0
listavoti1 = []
listavoti2 = []
while True:
    print("inserisci 1 se voti", c1, "o inserisci 2 se voti", c2)
    v = int(input("il tuo voto: "))
    if v == 1:
        listavoti1.append(v)
    if v == 2:
        listavoti2.append(v)
    voti = voti + 1
    if voti == nvoti:
        break
cont1 = len(listavoti1)
cont2 = len(listavoti2)
gg = cont1 + cont2
if cont1 >= cont2:
    perc1 = cont1*100/gg
    print("Ha vinto", c1, "con", cont1, "voti e una percentuale del", perc1, "%")
if cont2 >= cont1:
    perc2 = cont2*100/gg
    print("Ha vinto", c2, "con", cont2, "voti e una percentuale del", perc2, "%")
if cont2 == cont1:
    print("Pareggio tra", c1, "e", c2)

input("ES 2")

cand1 = input("Nome primo candidato: ")
cand2 = input("nome secondo candidato: ")
punt1 = int(input("punteggio primo candidato: "))
punt2 = int(input("punteggio secondo candidato; "))
listcand = []
listpunt = []
listcand.append(cand1)
listcand.append(cand2)
listpunt.append(punt1)
listpunt.append(punt2)
listpunt.sort()
listpunt.reverse()
print(listpunt)
listcand.sort()
print(listcand)

input("ES 3")

ndipend = 0
listguad = []
while True:
    print("quando hai finito digita -1")
    guad = int(input("quanto guadagna il dipendente?"))
    if guad != -1:
        ndipend = ndipend + 1
        listguad.append(guad)
        media = sum(listguad)/ndipend
        print(media)
    if guad == -1:
        print("la media è", media)
        break