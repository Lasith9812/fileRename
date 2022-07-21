import os
from numpy import size

start = int(input("Start Number: "))
end = int(input("End Number: "))

r = os.listdir(".")
cc = input("Split characters by: ")

print("Number of files in the directory:"+ str(size(r)))
r.remove("main.py")
try:
    for i in r:
        ext = str(i.split('.',-1)[1])
        k = (i.split(str(cc)))
        for j in k:
            for l in range(start,end):
                if j == str(l):
                    os.rename(str(i),j+"."+ext)
except:
    pass
