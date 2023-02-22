import random

#0
print("Osztályzatok generálása.")

#1
db=int(input("Kérem az osztályzatok számát: "))

osztalyzatok=[]
#mivel tudjuk a darabszámot ezért - előre meghatározott lépésszámú ciklus
for i in range(db):
    oszt = random.randint(1, 5) #az osztályzatok 1 - 5 terjednek
    osztalyzatok.append(oszt)

#2-3
print(osztalyzatok)
