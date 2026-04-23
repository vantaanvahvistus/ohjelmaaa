import math

def create_point(x, y):
    p = [x, y]
    return p

x1 = int(input("anna ensimmäisen pisteen x-koodrinaatti: "))
y1 = int(input("anna ensimmäisen pisteen y-koodrinaatti: "))
x2 = int(input("anna toisen pisteen x-koodrinaatti: "))
y2 = int(input("anna toisen pisteen y-koodrinaatti: "))

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

print(f"etäisyys: {distance(p1, p2):.2f}")