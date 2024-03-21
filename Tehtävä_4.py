import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        matkan_muutos = self.nykyinen_nopeus * tunnit
        self.kuljettu_matka += matkan_muutos

    def __str__(self):
        return (f"{self.rekisteritunnus}\t"
                f"{self.huippunopeus} km/h\t"
                f"{self.nykyinen_nopeus} km/h\t"
                f"{self.kuljettu_matka} km")


autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

# Kilpailu
kilpailu_jatkuu = True
while kilpailu_jatkuu:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_jatkuu = False

# Tulokset
print("Rekisteritunnus\tHuippunopeus\tTämänhetkinen Nopeus\tKuljettu Matka")
for auto in autot:
    print(auto)
