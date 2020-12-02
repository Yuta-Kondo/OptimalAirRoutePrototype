import math

mintime = math.inf  #最小時間は後から代入するため仮に∞と定義する

for i in range (0, 10000):
  for j in range (0, 10000):

    if i != j:  #j-iが0になると分母として扱えない。

      angle = math.atan(4000/abs(j-i))  #計算式
      v = -300 * math.cos(angle) + math.sqrt(90000 * math.cos(angle) * math.cos(angle) + 550000)
      time = math.sqrt(i**2 + 3000**2)/800 + math.sqrt((10000 - j)**2 + 3000**2)/800 + math.sqrt((j-i)**2 + 4000**2)/v

      if mintime > time:  #最短時間の場合は情報を記録
        mintime = time
        windpowered_velocity = v
        i_index = i
        j_index = j

print(mintime)
print("windpowered_velocity: " + str(windpowered_velocity))
print("i-index: " + str(i_index))
print("j-index: " + str(j_index))
