stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginpunt():
    global begin
    begin = input('Voer beginstation in. ')
    while True:
        if begin not in stations:
            print('Deze trein komt niet in {}. Probeer opnieuw.'.format(begin))
            begin = input('Voer beginstation in. ')
        else:
            return begin

def inlezen_eindpunt():
    global eind
    eind = input('Voer eindstation in. ')

    while True:
        if eind not in stations:
            print('Deze trein komt niet in {}. Probeer opnieuw.'.format(eind))
            eind = input('Voer eindstation in. ')
        elif stations.index(eind) <= stations.index(begin):
            print('Eindstation zit voor het beginstation, probeer opnieuw. ')
            print()
            eind = input('Voer eindstation in. ')
            return eind
        else:
            return eind

    print()

def omroepen_reis():

    afstand = (stations.index(eind) + 1) - (stations.index(begin) + 1)
    print('Het beginstation {} is het ' + str(stations.index(begin) + 1 ) + 'e station in het traject. '.format(begin))
    print('Het eindstaion {} is het ' + str(stations.index(eind) + 1) + 'e station in het traject. '.format(eind))
    print('De afstand bedraagt ' + str(afstand) + ' station(s). ')
    print('De prijs van het kaartje is ' + str(afstand * 5) + ' euro.')

    print()

    print('U stapt in de trein in: {}'.format(begin))

    for x in range((stations.index(begin) + 1), stations.index(eind)):
        print('  - ' + stations[x])

    print('U stapt uit de trein in: {}'.format(eind))

inlezen_beginpunt()

inlezen_eindpunt()

omroepen_reis()
