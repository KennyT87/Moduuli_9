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


uusi_auto = Auto("ABC-123", 142)
uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)
print(f"Auton nopeus: {uusi_auto.nykyinen_nopeus} km/h")

uusi_auto.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {uusi_auto.nykyinen_nopeus} km/h")
