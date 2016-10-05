# Owen, Alkmaar, Amsterdam Amstel

naam = input('Voer u voornaam in: ')
begin_station = input('Voer uw beginstation in: ')
eind_station = input('Voer uw eindstation in: ')

samenvoeg = naam + begin_station + eind_station

def code(inp):
    for letter in samenvoeg:
        asciiChar = ord(letter)
        encrypted = asciiChar + 3
        newChar = chr(encrypted)
        return newChar

print(code(samenvoeg), end='')
# Deel 2 van F.A. 6
#             geordend        muteerbaar      iterable        dubbele waarden toegestaan
# tuple       JA              NEE             JA              JA
# Dictionary  NEE             NEE             JA              NEE
# Set         NEE             NEE             JA              NEE
# List        JA              JA              JA              JA
