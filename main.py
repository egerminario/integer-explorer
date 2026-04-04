def valid_4bit(bits):
    return len(bits) == 4 and all(b in "01" for b in bits)

a = input("Enter 4-bit binary number A: ")
b = input("Enter 4-bit binary number B: ")

while not valid_4bit(a):
	a = input("Invalid input. Enter exactly 4 bits for A: ")
while not valid_4bit(b):
	b = input("Invalid input. Enter exactly 4 bits for B: ")

def unsigned(bits):
	return int(bits, 2)

def signed(bits):
	value = int(bits, 2)
	if bits[0] == "1":
		return value - 16
	return value

print("A unsigned =", unsigned(a))
print("A signed =", signed(a))
print("B unsigned =", unsigned(b))
print("B signed =", signed(b))
