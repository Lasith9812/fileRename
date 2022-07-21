import os

r = os.listdir(".")

print(r)

r.remove("main.py")

print(r)

for i in r:
    
    os.rename(i,)
