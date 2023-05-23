import pojisteni

while True:
    print('----------------------')
    print('Evidence pojištěných')
    print('----------------------')
    print('Vyberte si akci:')
    print('1 - Přidat nového pojištěného')
    print('2 - Vypsat všechny pojištěné')
    print('3 - Vyhlédat pojištěného')
    print('4 - Konec')

    volba = input()

    if volba == '1':
        pojisteni.pridat_pojisteneho()
        print('Data byla uložena. Pokračujte libovolnou klávesou....')
        input()

    elif volba == '2':
        pojisteni.vypsat_vsechny_pojistene()
        print('Pokračujte libovolnou klávesou....')
        input()

    elif volba == '3':
        pojisteni.vyhledat_pojisteneho()
        print('Pokračujte libovolnou klávesou....')
        input()

    elif volba == '4':
        break

    else:
        print('Neplatná volba, opakujte zadání....')
