import matplotlib.pyplot as plt
N_body = 8
f = open('D:\XYout.txt')
Orbits = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for str in f:
    Arr = str.split(' ')
    for i in range(2*N_body):
        Orbits[i].append(float(Arr[i]))
#строим графики
fig = plt.figure(figsize=(10,10))
for i in range(0, 2*N_body, 2):
    plt.plot(Orbits[i], Orbits[i+1])
plt.axis('square')
plt.xlabel('AU')
plt.ylabel('AU')
plt.show()
