import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

# Dados para plotar

salaries = [1215, 1221, 1263, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324,
1326, 1337, 1346, 1354, 1355, 1364, 1367, 1372, 1375, 1376, 1378,
1378, 1410, 1415, 1415, 1418, 1420, 1422, 1426, 1430, 1434, 1437,
1451, 1454, 1467, 1470, 1473, 1477, 1479, 1480, 1514, 1516, 1522,
1529, 1544, 1547, 1554, 1562, 1584, 1595, 1616, 1626, 1717]


count , labels = np.histogram(salaries, bins=np.arange(1100, 1900, 50))

labels = ['$' + str(labels[i])+ '-' + '$' + str(labels[i+1]) for i, _ in enumerate(labels[:labels.__len__()-1])]

non_zeros_pos = [ i for i,x in enumerate(count) if x != 0]

print(count)
print(labels)
print(non_zeros_pos)

labels = [e for i , e in enumerate(labels) if i in non_zeros_pos]
count = [e for i , e in enumerate(count) if i in non_zeros_pos]

plt.pie(count, labels=labels ,autopct='%1.1f%%')
plt.title("Proporção dos salários mensais no departamento")
plt.show()

new_count = []
new_label = []
total_other = 0

for i, value in enumerate(count):
    if ( value < 3 ):
        total_other += value
    else:
        new_count.append(count[i])
        new_label.append(labels[i])

new_label.append("Others")
new_label.append(total_other)

plt.pie(new_count, labels=new_label, autopct='%1.1f%%')
plt.show()