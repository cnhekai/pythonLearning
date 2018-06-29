names = ['kai','feng','jiang']

for name in names:
  print('我是for循环：' + name)

sum = 0
n = 100
while n > 0:
  sum += n
  n -= 1
print('whild的值为：' + str(sum))

sum = 0
for a in range(100):
  sum += a
  if a > 10:
    print('使用break跳出循环时sum的值：', sum)
    break

sum = 0
n = 0
while n <= 100:
  n += 1
  if n % 2 == 0:
    continue
  sum += n
print('使用continue得到0到100所有的奇数和:', sum)
