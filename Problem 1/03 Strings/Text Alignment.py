thickness = int(input())

for i in range(0, thickness):
    print(("H"*(2*i+1)).center(thickness*2-1, " "))

for i in range(0, thickness+1):
    print(("H"*thickness).center(thickness*2, " ") + ("H"*thickness).center(thickness*6, " "))

for i in range(0, (thickness+1)//2):
    print(("H"*thickness*5).center(thickness*6), " ")

for i in range(0, thickness+1):
    print(("H"*thickness).center(thickness*2, " ") + ("H"*thickness).center(thickness*6, " "))

for i in range(thickness-1, -1, -1):
    print((" "*thickness).center(thickness*4, " ") + ("H"*(2*i+1)).center(thickness*2, " "))
