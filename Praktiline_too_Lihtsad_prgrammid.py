from datetime import *
from calendar import *
from math import *

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


