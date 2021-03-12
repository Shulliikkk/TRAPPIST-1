import matplotlib.pyplot as plt
f = open('D:\Energy.txt')
E = []
s = []
begin = True
for str in f:
    Arr = str.split(' ')
    if begin == True:
        E0 = float(Arr[0])
        begin = False
    E.append((float(Arr[0])-E0)/E0)
    s.append(float(Arr[1]))
fig = plt.figure(figsize=(5,5))
plt.plot(s, E)
plt.xlabel('step')
plt.ylabel('energy divergence')
plt.show()
