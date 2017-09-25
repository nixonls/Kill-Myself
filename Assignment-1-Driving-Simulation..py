t = int(input("time spent on the road"))
a = int(input("acceleration"))
d = int(input("distance"))
count = 0
dis = (a * (t ** 2)) / 2
vel = a * t

for n in range(0, t + 1):
    dis2 = ((a * (n ** 2)) / 2) / 10
    print('Duration: ', n, 'Distance: ', '*' * int(dis2))

s = int(60)
if vel > s:
    print('The person went over the speed limit (Max speed was = ', vel, 'm/s)')
else:
    print('The person did not go over the speed limit (Max speed was = ', vel, 'm/s')

if (dis < d):
    print("The person reached the destination (Reached : ", dis, 'm')

else:
    print("The person did not reach the destination (Reached : ", dis, 'm')
