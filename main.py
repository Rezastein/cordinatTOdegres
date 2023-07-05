import os
import time


def cl():
    os.system("cls")


xd = 6
yd = 107
cl()
print('\n'*3)
xm = int(input("mS: "))
ym = int(input("mE: "))

file1 = open('lat.txt', 'a')
file2 = open('long.txt', 'a')

count = int(input("Count: "))

for i in range(count):
    cl()
    print('\n'*3)
    xs = float(input("sS: "))
    ys = float(input("sE: "))
    s = xd + (xm/60) + (xs/3600)
    e = yd + (ym/60) + (ys/3600)

    lat = [f'-{s}\n']
    log = [f'{e}\n']

    file1.writelines(lat)
    file2.writelines(log)

file1.close()
file2.close()

with open('lat.txt', 'r') as lt:
    lat_ = lt.readlines()
for v in lat:
    print(v)
with open('long.txt', 'r') as lg:
    long_ = lg.readlines()
for z in long_:
    print(z)

os.system('python3 pushexcle.py')
os.system('start EXCEL.EXE sample.xlsx')
os.system('timeout /t 120 /nobreak')
