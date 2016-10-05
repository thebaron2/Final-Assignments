import random
import csv
#keuze 1
def nieuwe_kluis():
    with open('kluizen_fa7.csv', 'r', newline='') as kluizen:
        reader = csv.reader(kluizen, delimiter=';')

        bezette_kluis_nummers = []

        for row in reader:
            bezette_kluis_nummers.append(row[0])

        if len(bezette_kluis_nummers) > 12:
            print('Er zijn momenteel geen kluizen beschikbaar! ')
        else:
            while True:
                kluisNummer = input('Welke kluis wilt u? ')
                if kluisNummer in bezette_kluis_nummers:
                    print('Helaas, kluis {} is niet beschikbaar.'.format(kluisNummer))
                    print()
                else:   #generatie van de code
                    nummer1 = random.randrange(0, 10)
                    nummer2 = random.randrange(0, 10)
                    nummer3 = random.randrange(0, 10)
                    nummer4 = random.randrange(0, 10)
                    kluis_code = '{}{}{}{}'.format(nummer1, nummer2, nummer3, nummer4)
                    print('Uw code is: {}'.format(kluis_code))
                    print()

                    with open('kluizen_fa7.csv', 'a', newline='') as kluizen2:
                        wr = csv.writer(kluizen2, delimiter=';')
                        tuple = (kluisNummer, kluis_code)
                        wr.writerow(tuple)
                    break
# keuze 2
def kluis_openen():
    with open('kluizen_fa7.csv', 'r', newline='') as kluizen:
        reader = csv.reader(kluizen, delimiter=';')

        kluis_dict = {}

        for row in reader:
            kluis_dict[row[1]] = row[0]

        while True:
            ingevoerde_code = input('Voer uw 4 cijferige code in: ')

            if ingevoerde_code in kluis_dict:
                print('Uw kluis met nummer ' + kluis_dict.get(ingevoerde_code) + ' is nu open.')
                print()
                break
            else:
                print('Ongeldige code ingevoerd! Probeer opnieuw.')
                print()
# keuze 3
def kluis_teruggeven():
    with open('kluizen_fa7.csv', 'r', newline='') as kluizen:
        reader = csv.reader(kluizen, delimiter=';')

        blijvende_kluizen = []
        ingevoerde_code = input('Voer uw 4 cijferige code in: ')

        for row in reader:
            if ingevoerde_code != row[1]:
                blijvende_kluizen.append(row)
        print('Kluis {} is nu vrijgegeven.'.format(row[0]))
        print()

        with open('kluizen_fa7.csv', 'w', newline='') as kluizen:
            wr = csv.writer(kluizen, delimiter=';')
            wr.writerows(blijvende_kluizen)
# keuze 4
def aantal_kluizen_vrij():
    with open('kluizen_fa7.csv', 'r', newline='') as kluizen:
        reader = csv.reader(kluizen, delimiter=';')

        bezette_kluis_nummers = []

        for row in reader:
            bezette_kluis_nummers.append(row[0])

        if len(bezette_kluis_nummers) >=12:
            print('Er zijn momenteel geen kluizen beschikbaar! ')
        else:
            kluizen_over = 12 - len(bezette_kluis_nummers)
            print('Er zijn {} van de 12 kluizen over.'.format(kluizen_over))
            print()
# het menu
while True:
    keuze = input('1: Ik wil een nieuwe kluis.\n'
                  '2: Ik wil mijn kluis openen.\n'
                  '3: Ik geef mijn kluis terug.\n'
                  '4: Ik wil weten hoeveel kluizen nog vrij zijn.\n'
                  '5: Ik wil stoppen.\n'
                  '\n'
                  'Geef het getal van uw keuze: ')
    try:
        if int(keuze) == 1:
            nieuwe_kluis()
        if int(keuze) == 2:
            kluis_openen()
        if int(keuze) == 3:
            kluis_teruggeven()
        if int(keuze) == 4:
            aantal_kluizen_vrij()
        if int(keuze) == 5:
            break
    except ValueError:
        print('Uw heeft geen getal ingevoerd!\n'
              'Probeer een getal!'
              '\n')
    except:
        print('Er ging iets mis bij de file, probeer daar een regel weg te halen.'
              '\n')
