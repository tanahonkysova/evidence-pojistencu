from pojisteny import Pojisteny

pojisteni = []

def pridat_pojisteneho():
    jmeno = input('Zadejte jméno: ')
    while not jmeno or not jmeno.isalpha():
        if not jmeno:
            print('Jméno nemůže být prázdné')
        else:
            print('Jméno musí být zadáno pouze písmeny')
        jmeno = input('Zadejte jméno: ')


    prijmeni = input('Zadejte příjmení: ')
    while not prijmeni or not prijmeni.isalpha():
        if not prijmeni:
            print('Příjmení nemůže být prázdné')
        else:
            print('Příjmení musí být zadáno pouze písmeny')
        prijmeni = input('Zadejte příjmení: ')

    telefonni_cislo = input('Zadejte telefonní číslo: ')
    while not telefonni_cislo or not telefonni_cislo.isdigit():
        if not telefonni_cislo:
            print('Telefonní číslo nemůže být prázdné')
        else:
            print('Pro zadání telefonního čísla použijte číslice')
        telefonni_cislo = input('Zadejte telefonní číslo: ')

    vek = input('Zadejte věk: ')
    while not vek or not vek.isdigit():
        if not vek:
            print('Věk nemůže být prázdný')
        else:
            print('Pro zadání věku  použijte číslice')
        vek = input('Zadejte věk: ')
    pojisteny = Pojisteny(jmeno, prijmeni, telefonni_cislo, vek)
    pojisteni.append(pojisteny)

def vypsat_vsechny_pojistene():
    if not pojisteni:
        print('Evidence je prázdná')
        return

    poj_seznam = [[str(p.jmeno), str(p.prijmeni), str(p.telefonni_cislo), str(p.vek)] for p in pojisteni]
    widths = [max(map(len, col)) for col in zip(*poj_seznam)]
    for zaznam in poj_seznam:
        print("  ".join((val.ljust(width) for val, width in zip(zaznam, widths))))


def vyhledat_pojisteneho():
    if not pojisteni:
        print('Evidence je prázdná')
        return

    jmeno = input('Zadejte jméno pojištěného: ')
    while not jmeno:
        print('Jméno nemůže být prázdné')
        jmeno = input('Zadejte jméno pojištěného: ')

    prijmeni = input('Zadejte příjmení: ')
    while not prijmeni:
        print('Příjmení nemůže být prázdné')
        prijmeni = input('Zadejte příjmení: ')

    nalezeno = False
    for p in pojisteni:
        if p.jmeno.lower() == jmeno.lower() and p.prijmeni.lower() == prijmeni.lower():
            print(p)
            nalezeno = True
            break

    if not nalezeno:
        print('Pojištěný nebyl nalezen v evidenci.')


def upravit_pojisteneho(jmeno, prijmeni):
    for p in pojisteni:
        if p.jmeno == jmeno and p.prijmeni == prijmeni:
            nove_jmeno = input('Zadejte nové jméno: ')
            nove_prijmeni = input('Zadejte nové příjmení: ')
            nove_telefonni_cislo = input('Zadejte nové telefonní číslo: ')
            nove_vek = input('Zadejte nový věk: ')

            p.jmeno = nove_jmeno
            p.prijmeni = nove_prijmeni
            p.telefonni_cislo = nove_telefonni_cislo
            p.vek = nove_vek

            print('Data byla aktualizována. Pokračujte libovolnou klávesou....')
            input()
            return

    print('Pojištěný nebyl nalezen. Pokračujte libovolnou klávesou....')
    input()

def odstranit_pojisteneho(jmeno, prijmeni):
    for i in range(len(pojisteni)):
        if pojisteni[i].jmeno == jmeno and pojisteni[i].prijmeni == prijmeni:
            del pojisteni[i]

            print('Pojištěný byl odstraněn. Pokračujte libovolnou klávesou....')
            input()
            return

    print('Pojištěný nebyl nalezen. Pokračujte libovolnou klávesou....')
    input()
