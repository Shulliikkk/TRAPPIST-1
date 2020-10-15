import math
import matplotlib.pyplot as plt
N_bodyes = 8 #количество тел в системе
Time = 2 #время в сутках
dt = 0.0001 #шаг
N_steps = Time/dt #количество итераций
G = 8.89042 * 10**-10 #гравитационная постоянная
Pi = math.pi
k = Pi/180 #константа для перевода градусов в радианы

m = [29600, 0.79, 1.63, 0.33, 0.24, 0,4, 0.566, 0.04] #массы планет, выраженные в земных массах, первый элемент - масса звезды
r = [0.0, 0.0115, 0.01576, 0.02219, 0.02916, 0.03836, 0.0467, 0.0617] #большие полуоси орбит (их радиусы, т.к. мы считаем их круговыми)
phase = [0.0, 0.0, 217.470, 300.378, 142.558, 323.471, 269.932, 42.487] #начальные фазы планет
T = [1.0, 1.51087637, 2.42180746, 4.049959, 6.099043, 9.205585, 12.354473, 18.767953] #периоды обращения планет в сутках

position = [[[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []],[[], []]] #массив для удобного доступа к координатам каждого тела

#массивы, хранящие проекции скоростей всех тел в текущий момент времени
vx = []
vy = []


#цикл, задающий начальные координаты и скорости
for i in range(0, N_bodyes):
  x = position[i][0] #выражение, выцепляющее из общего массива position массив, хрянящий координаты X i-го тела
  y = position[i][1] #выражение, выцепляющее из общего массива position массив, хрянящий координаты Y i-го тела
  x.append(r[i] * math.cos(phase[i] * k))
  y.append(r[i] * math.sin(phase[i] * k))
  vx.append(-(2 * r[i] * Pi / T[i] * math.sin(phase[i] * k)))
  vy.append(2 * r[i] * Pi / T[i] * math.cos(phase[i] * k))

#основной цикл
sum1 = 0
sum2 = 0
step = 1
while step <= N_steps + 1:
  for i in range(0, N_bodyes):
      xi = position[i][0]
      xi.append(xi[len(xi)-1] + vx[i] * dt) #добавляем в конец списка xi координаты тела на момент времени step * dt
      yi = position[i][1]
      yi.append(yi[len(yi)-1] + vy[i] * dt) #добавляем в конец списка yi координаты тела на момент времени step * dt


      for k in range(0, N_bodyes):
          if i == k:
              continue
          xk = position[k][0]
          yk = position[k][1]
          #суммы, стоящие за знаком суммирования в формулах
          sum1 = sum1 + ( m[k] / ((xk[len(xk)-2] - xi[len(xi)-2])**2 + (yk[len(yk)-2] - yi[len(yi)-2])**2)**1.5 * (yk[len(xk)-2] - xi[len(xi)-2]) )
          sum2 = sum2 + ( m[k] / ((xk[len(xk)-2] - xi[len(xi)-2])**2 + (yk[len(yk)-2] - yi[len(yi)-2])**2)**1.5 * (yk[len(yk)-2] - yi[len(yi)-2]) )

       #поправки к текущей скорости
      dvx = G * sum1 * dt
      dvy = G * sum2 * dt

       #подправляем скорости
      vx[i] = vx[i] + dvx
      vy[i] = vy[i] + dvy

      sum1 = 0
      sum2 = 0
  step += 1

#строим графики
fig = plt.figure(figsize=(10,10))
plt.plot(position[0][0], position[0][1], position[1][0], position[1][1], position[2][0], position[2][1], position[3][0], position[3][1], position[4][0], position[4][1], position[5][0], position[5][1], position[6][0], position[6][1], position[7][0], position[7][1])
plt.show()
