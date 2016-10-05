ritten = open('treinritten.txt', 'r')
ritten_content = ritten.readlines()
ritten.close()

annuleringen = open('annuleringen.txt', 'r')
annuleringen1 = annuleringen.readlines()
annuleringen.close()

annuleringenList = []
herzien = []

for canceled in annuleringen1:
    annuleringenList.append(canceled.rstrip().split(': ')[1])

for bestemming in ritten_content:
    bestemming1 = bestemming.rstrip().split(' - ')[1]
    if (annuleringenList.count(bestemming1) == 0):
        herzien.append(bestemming)

herzienFile = open('treinritten2.txt', 'w')
herzienFile.writelines(herzien)
herzienFile.close()
