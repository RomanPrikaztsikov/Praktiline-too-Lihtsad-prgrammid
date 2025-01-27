from datetime import *
from calendar import *
from math import *

#10
try:
    minutid=int(input("Sisesta aeg minutites: "))
    if minutid<=0:
        print("Vale arv!")
    else:
        tunnid=minutid//60
        jääk_minutid=minutid % 60
        print(f"{minutid} minutit on {tunnid},{jääk_minutid}")

except:
    print("Palun sisesta täisarv!")



#9
kiirus_kmh=29.9
meetrit_per_minut=(kiirus_kmh * 1000)/60
print(f"Rulluisutaja läbib ühe minutiga {meetrit_per_minut} meetrit")


#8
try:
    kütus=float(input("Sisesta kütusekogus liitrites: "))
    kilomeetrid=float(input("Sisesta läbitud kilomeetrid: "))
    if kütus <=0 or kilomeetrid <=0:
        print("Vale numbrid! Nad peavad olema positivseed.")
    else:
        kütusekulu_100km = (kütus / kilomeetrid)*100
        print(f"Kütusekulu 100 km kohta on: {kütusekulu_100km} liitrit")

except:
    print("Vale andmed!.")



#7
try:
    a=float(input("a: "))
    b=float(input("b: "))
    if a>0 and b>0:
        print("Arvutamine")
        S=a*b
        P=(a+b)*2
        print(f"S={S}, P={P}")
    else:
         print("Arvud peavad suurem kui 0 olla!")
except:
    print("Vale andmed!")
    



# #6
# print('''Rong see sõitis tsuhh tsuhh tsuhh,
# piilupart oli rongijuht.
# Rattad tegid rat tat taa,
# rat tat taa ja tat tat taa.
# Aga seal rongi peal,
# kas sa tead, kes olid seal?

# Rong see sõitis tuut tuut tuut,
# piilupart oli rongijuht.
# Rattad tegid kill koll koll,
# kill koll koll ja kill koll kill.''').capitalize()




#5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)

#4
d=2.575
maaR=6378
maaR*=100000
Pmaa=2*pi*maaR
kogus=Pmaa/d
print(f"Mel on vaja {int(kogus):,d} mündi. ")
print(f"Mel on vaja {int(kogus*2):,d} euro. ")

#"Ülesanne 3"
try:
   R=float(input("R: "))
   Sruudu=round((2*R)**2,2)
   Sringi=round(pi*R**2,2)
   Pruudu=round(8*R,2)
   Pringi=round(2*pi*R,2)
   print(f"Vastus:\nRuudu pindala on {Sruudu}, ruudu umbermõõt on {Pruudu}, \nRingi pindala on {Sringi}, Ringi umbermõõt on {Pringi}.")
   print()
except:
    print("Sisesta ujukomaarvud!")


#1
tana = date.today()
tana_1 = tana.strftime("%d/%m/%Y")
print(f"Tere! Täna on {tana_1}")

paevadekogus=monthrange(2025,1)[1]
print(f"Jaanuaris on {paevadekogus} päeva")
päevad=tana.day
onjäänud=paevadekogus-päevad
print(f"Jaanuaris on jäänud {onjäänud} päeva")

aastalõppuni=365-monthrange(2025,1)[1]+onjäänud
print(f"Aasta lõpuni on jäänud {aastalõppuni}")

#2
tulemus=3+8/(4 - 2)*4
print(f"tulemus on 3+8/(4 - 2)*4 = {tulemus}") #sulgudes lahutamine

tulemus=3+8/4 - 2*4
print(f"tulemus on 3+8/4 - 2*4 = {tulemus}") #sulgudeta

tulemus=(3+8)/4 - 2*4
print(f"tulemus on (3+8)/4 - 2*4 = {tulemus}") #lisamine sulgudes

tulemus=3+8/(4 - 2*4)
print(f"tulemus on 3+8/(4 - 2*4) = {tulemus}") #teine ​​osa sulgudes


# tana_2 = tana.strftime("%B %d, %Y")
# print(f"Tere! Täna on {tana_2}")

# tana_3 = tana.strftime("%b-%d-%Y")
# print(f"Tere! Täna on {tana_3}")

# tana_4 = tana.strftime("%m/%d/%y")
# print(f"Tere! Täna on {tana_4}")


