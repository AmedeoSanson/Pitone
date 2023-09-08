SECONDI_IN_MINUTO = 60
SECONDI_IN_ORA = SECONDI_IN_MINUTO * 60
SECONDI_IN_GIORNO = SECONDI_IN_ORA * 24
SECONDI_IN_ANNO = SECONDI_IN_GIORNO * 365

istante1 = {
    "anno": 2021,
    "mese": 5,
    "giorno": 3,
    "ora": 15,
    "minuto": 22,
    "secondo": 36
}
istante2 = {
    "anno": 2022,
    "mese": 1,
    "giorno": 3,
    "ora": 9,
    "minuto": 18,
    "secondo": 30
}

giorniAlMese = (31,28,31,30,31,30,31,31,30,31,30,31)

# SUGGERIMENTO: Trasforma entrambe le date in secondi passati dal 01/01/2000 e fai la differenza

#primo istante
anniInSec = (istante1["anno"] - 2000 + 1) * SECONDI_IN_ANNO # L'ultimo anno non va contato
giorniInSec = (istante1["mese"] - 1) * SECONDI_IN_GIORNO # L'ultimo giorno non va contato
oreInSec = (istante1["ora"]) * SECONDI_IN_ORA
minutiInSec = (istante1["minuto"]) * SECONDI_IN_MINUTO

secondiDeiMesi = 0
for i in range(istante1["mese"]):
    secondiDeiMesi += giorniAlMese[i] * SECONDI_IN_GIORNO

giorniBisestili = (istante1["anno"] - 2000)/4
if(istante1["mese"] > 2):
    giorniBisestili += 1
secondiDeiBisestili = giorniBisestili * SECONDI_IN_GIORNO

istante1InSec = anniInSec + secondiDeiMesi + giorniInSec + oreInSec + minutiInSec + istante1["secondo"] + secondiDeiBisestili

#secondo istante
anniInSec = (istante2["anno"] - 2000 + 1) * SECONDI_IN_ANNO # L'ultimo anno non va contato
giorniInSec = (istante2["mese"] - 1) * SECONDI_IN_GIORNO # L'ultimo giorno non va contato
oreInSec = (istante2["ora"]) * SECONDI_IN_ORA
minutiInSec = (istante2["minuto"]) * SECONDI_IN_MINUTO

secondiDeiMesi = 0
for i in range(istante2["mese"]):
    secondiDeiMesi += giorniAlMese[i] * SECONDI_IN_GIORNO

giorniBisestili = (istante2["anno"] - 2000)/4
if(istante2["mese"] > 2):
    giorniBisestili += 1
secondiDeiBisestili = giorniBisestili * SECONDI_IN_GIORNO

istante2InSec = anniInSec + secondiDeiMesi + giorniInSec + oreInSec + minutiInSec + istante2["secondo"] + secondiDeiBisestili


differenzaInSecondi = istante2InSec - istante1InSec

print(differenzaInSecondi)


