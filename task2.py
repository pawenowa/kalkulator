#!/usr/bin/python3
print('Sprawdź czy uczeń jest w bazie i wyświetl oceny')
nazwisko = input("Podaj nazwisko ucznia: ")
uczniowie = {'Kowalski': ['1', '3', '3.5'], 'Nowak': ['3', '5', '4'], 'Maliszewski': ['5', '5', '6']}
if nazwisko not in uczniowie: 
    print ('Brak danych')
    exit()    
print('Oceny ucznia: ')
print('\n'.join(uczniowie[nazwisko]))

