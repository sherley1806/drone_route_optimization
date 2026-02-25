import math
import itertools
print("Drone Route Optimization System")
sx = float(input("Enter starting X: "))
sy = float(input("Enter starting Y: "))
n = int(input("Enter number of delivery points: "))
points = []
for i in range(n):
    print(f"\nDelivery Point {i+1}")
    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))
    points.append((x, y))
# Distance function (FIXED)
def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
best_route = None
best_distance = float('inf')
# Route permutations loop (FIXED)
for order in itertools.permutations(points):
    total = 0
    current = (sx, sy)

    for p in order:
        total += dist(current, p)
        current = p

    if total < best_distance:
        best_distance = total
        best_route = order


print("\n--- Optimal Route Found ---")
print("Shortest distance:", round(best_distance, 2), "km")
print("Visit points in this order:")

for p in best_route:
    print(p)