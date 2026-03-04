from auto import Auto
import random

auto1 = Auto("Toyota", "Corolla", 2015, 6.5)
auto2 = Auto("Volkswagen", "Passat", 2002, 4.5)
auto3 = Auto("Audi", "E-tron GT", 2021, 0)
auto4= Auto("Bugatti", "Veyron", 2007, 18)

# print(auto1)
# print(auto2)
# print(auto3)

# auto1.gyorsit(150)

# print(auto1)

# auto1.gyorsit(150)

# print(auto1)


autok = [auto1, auto2, auto3, auto4]
for auto in autok:
    print(auto)


print("\nGyorsít\n")
for auto in autok:
    auto.gyorsit(random.randint(30,150))
    print(auto)

ossz_eletkor = 0
autok_szama = len(autok)
for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    ossz_eletkor += kor

atlag_eletkor = ossz_eletkor / autok_szama
print(f"Az autók átlegéletkora: {atlag_eletkor} év")

legidosebbb_auto = None
legidosebbb_auto_kora = 0

for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    if kor > legidosebbb_auto_kora:
        legidosebbb_auto_kora = kor
        legidosebbb_auto = auto

print(f"A legidősebb autó kora: {legidosebbb_auto_kora}, adatai: {legidosebbb_auto}")


