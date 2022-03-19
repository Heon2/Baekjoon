x, y, w, h = map(int, input().split())

a = y
b = w-x
c = h-y
d = x

result = min(a, b, c, d)
print(result)
