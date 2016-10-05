stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

begin = input('Voer beginstation in. ')
if begin not in stations:
    print('Ongeldig beginstation, beginstation is: Schagen!')
    begin = stations[0]

eind = input('Voer eindstation in. ')
if eind not in stations:
    print('Ongeldig eindstation, eindstation is: Maastricht!')
    eind = stations[-1]

print()

if stations.index(eind) <= stations.index(begin):
    print('Eindstation zit voor het beginstation, eindstation is: Maastricht! ')
    eind = stations[-1]

afstand = (stations.index(eind) + 1) - (stations.index(begin) + 1)
print('Het beginstation ' + begin + ' is het ' + str(stations.index(begin) + 1 ) + 'e station in het traject. ')
print('Het eindstaion ' + eind + ' is het ' + str(stations.index(eind) + 1) + 'e station in het traject. ')
print('De afstand bedraagt ' + str(afstand) + ' station(s). ')
print('De prijs van het kaartje is ' + str(afstand * 5) + ' euro.')

print()

print('U stapt in de trein in: ' + begin)

for x in range((stations.index(begin) + 1), stations.index(eind)):
    print('  - ' + stations[x])

print('U stapt uit de trein in: ' + eind)
