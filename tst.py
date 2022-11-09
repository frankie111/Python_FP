a = -10
b = -10
c = 0x000FFFFF
x = -300

print("a*a = " + hex(a * a))
print("a * a + b = " + hex(a * a + b))
print("a * a + b + x = " + hex(a * a + b + x))
print("b+b = " + hex(b + b))
print("(a * a + b + x) // (b + b)) = " + hex((a * a + b + x) // (b + b)))
print("c+c = " + hex(c + c))
print("(a * a + b + x) // (b + b) + c * c = " + hex((a * a + b + x) // (b + b) + c * c))
