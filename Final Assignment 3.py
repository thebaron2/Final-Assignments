def standaardPrijs(afstandKM):
    if afstandKM < 0:
        return afstandKM * 0
    if afstandKM > 50:
        return 15 + (afstandKM * 0.60)
    if afstandKM <= 50:
        return afstandKM * 0.80


def ritPrijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == 'Ja':
        if leeftijd < 12:
            return (standaardPrijs(afstandKM) / 100) * 65
        if leeftijd >= 65:
            return (standaardPrijs(afstandKM) / 100) * 65
        else:
            return (standaardPrijs(afstandKM) / 100) * 60
    if weekendrit == 'Nee':
        if leeftijd < 12:
            return (standaardPrijs(afstandKM) / 100) * 70
        if leeftijd >= 65:
            return (standaardPrijs(afstandKM) / 100) * 70
        else:
            return (standaardPrijs(afstandKM))

print(ritPrijs(11, 'Ja', 0))
print(ritPrijs(11, 'Ja', -25))
print()
print(ritPrijs(11, 'Ja', 25))
print(ritPrijs(11, 'Nee', 25))
print()
print(ritPrijs(12, 'Ja', 25))
print(ritPrijs(12, 'Nee', 25))
print()
print(ritPrijs(64, 'Ja', 25))
print(ritPrijs(64, 'Nee', 25))
print()
print(ritPrijs(65, 'Ja', 25))
print(ritPrijs(65, 'Nee', 25))
print()
print(ritPrijs(11, 'Ja', 100))
print(ritPrijs(11, 'Nee', 100))
print()
print(ritPrijs(12, 'Ja', 100))
print(ritPrijs(12, 'Nee', 100))
print()
print(ritPrijs(64, 'Ja', 100))
print(ritPrijs(64, 'Nee', 100))
print()
print(ritPrijs(65, 'Ja', 100))
print(ritPrijs(65, 'Nee', 100))
