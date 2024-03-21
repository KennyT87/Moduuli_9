class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0


uusi_auto = Auto("ABC-123", 142)
print(uusi_auto)

print(f"Rekisteritunnus: {uusi_auto.rekisteritunnus}\n"
                f"Huippunopeus: {uusi_auto.huippunopeus} km/h\n"
                f"Tämänhetkinen nopeus: {uusi_auto.nykyinen_nopeus} km/h\n"
                f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")