print(pow(101, 17, 22663))

N = 17 * 23
e = 65537

print(pow(12, e, N))

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

phi = (p - 1) * (q - 1)
print(phi)

d = pow(e, -1, phi) # This is the modular inverse

print(d)