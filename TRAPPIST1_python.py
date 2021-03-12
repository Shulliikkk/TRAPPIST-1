# изучение стабильности планетной системы TRAPPIST-1
import math
import matplotlib.pyplot as plt
N_bodyes = 8 # количество тел в системе
Time = 30 # время в сутках
dt = 0.00001 #
N_steps = Time/dt # количество итераций
G = 8.89042 * 10**-10 # гравитационная постоянная
Pi = math.pi
k = Pi/180 # константа для перевода градусов в радианы

# массы планет, выраженные в земных массах, первый элемент - масса звезды
m = [29600, 0.79, 1.63, 0.33, 0.24, 0,4, 0.566, 0.04]
# большие полуоси орбит (их радиусы, т.к. мы считаем их круговыми)
r = [0.0, 0.0115, 0.01576, 0.02219, 0.02916, 0.03836, 0.0467, 0.0617]
# начальные фазы планет
phase = [0.0, 0.0, 217.470, 300.378, 142.558, 323.471, 269.932, 42.487]
# периоды обращения планет в сутках
T = [1.0, 1.51087637, 2.42180746, 4.049959, 6.099043, 9.205585, 12.354473, 18.767953]

# массив для удобного доступа к координатам каждого тела
positions = [[[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []],[[], []]]

# массивы, хранящие проекции скоростей всех тел в текущий момент времени
vx = []
vy = []

# цикл, задающий начальные координаты и скорости
for i in range(N_bodyes):
    # выражения, "выцепляющие" из общего массива position массив, хрянящий координаты x и y i-го тела
  x = positions[i][0]
  y = positions[i][1]

  x.append(r[i]*math.cos(phase[i]*k))
  y.append(r[i]*math.sin(phase[i]*k))
  vx.append(-(2*r[i]*Pi*math.sin(phase[i]*k)/T[i]))
  vy.append(2*r[i]*Pi*math.cos(phase[i]*k)/T[i])

# основной цикл
sum1, sum2, step = 0, 0, 1
while step <= N_steps:
  for i in range(0, N_bodyes):
      xi = positions[i][0]
      xi.append(xi[len(xi)-1] + vx[i]*dt) # добавляем в конец списка xi координаты тела на момент времени step*dt
      yi = positions[i][1]
      yi.append(yi[len(yi)-1] + vy[i]*dt) # добавляем в конец списка yi координаты тела на момент времени step*dt

      for k in range(0, N_bodyes):
          if i == k: continue
          xk = positions[k][0]
          yk = positions[k][1]
          # суммы, стоящие за знаком суммирования в формулах
          sum1 += (m[k]*(yk[len(xk)-2]-xi[len(xi)-2]) / ((xk[len(xk)-2]-xi[len(xi)-2])**2 + (yk[len(yk)-2]-yi[len(yi)-2])**2)**1.5)
          sum2 += (m[k]*(yk[len(yk)-2]-yi[len(yi)-2]) / ((xk[len(xk)-2]-xi[len(xi)-2])**2 + (yk[len(yk)-2]-yi[len(yi)-2])**2)**1.5)

       # подправляем скорости
      vx[i] = vx[i] + G*sum1*dt
      vy[i] = vy[i] + G*sum2*dt

      sum1, sum2 = 0, 0
  step += 1

#строим графики
fig = plt.figure(figsize=(10,10))
plt.axis('square')
plt.xlabel('AU')
plt.ylabel('AU')
for i in range(N_bodyes):
    plt.plot(positions[i][0], positions[i][1])
plt.show()
