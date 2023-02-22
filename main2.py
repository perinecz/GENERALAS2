import random

#0
print("Véletlen dátum generálása: 2005-2010 között.")

#1
ev=random.randint(2005, 2010)
honap=random.randint(1, 12)
nap=random.randint(1, 28) #mert február mindig tartalmaz 28-át
datum=f"{ev}.{honap:0>2d}.{nap:0>2d}"


#2-3
print(datum)
