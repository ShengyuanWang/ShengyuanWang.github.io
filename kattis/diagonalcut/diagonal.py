import math

a, b = map(int,input().strip().split()) 
res = math.gcd(2*a, 2*b) - math.gcd(a, 2*b) - math.gcd(2*a, b) + math.gcd(a, b)

print(res)