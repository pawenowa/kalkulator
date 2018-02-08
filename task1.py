#!/usr/bin/python3
print("Kalkulator ceny produktu bez VAT")
cena = float(input("Cena produktu z VAT (w PLN): "))
vat = float(input("Wysokość procentowa VAT: "))
vat /= 100
bez_vat = cena / (1 + vat)
print("Cena produktu bez VAT:" + str(bez_vat), "PLN")
