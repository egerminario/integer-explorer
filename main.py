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

def ones_complement(bits):
	flipped = ""
	for b in bits:
		if b == "0":
			flipped += "1"
		else:
			flipped += "0"
	return flipped

def twos_complement(bits):
	ones = ones_complement(bits)
	value = int(ones, 2) + 1
	return format(value & 0b1111, "04b")

def add_4bit(a, b):
	total = int(a, 2) + int(b, 2)
	carry_out = 1 if total > 15 else 0
	result = format(total & 0b1111, "04b")
	return result, carry_out

print("A unsigned =", unsigned(a))
print("A signed =", signed(a))
print("B unsigned =", unsigned(b))
print("B signed =", signed(b))

b_twos = twos_complement(b)
result, carry = add_4bit(a, b_twos)

print("B one's complement =", ones_complement(b))
print("B two's complement =", b_twos)
print("A - B result =", result)
print("Result unsigned =", unsigned(result))
print("Result signed =", signed(result))
print("Carry out =", carry)

if carry == 0:
    print("Unsigned borrow/underflow: YES")
else:
    print("Unsigned borrow/underflow: NO")

if (signed(a) - signed(b)) < -8 or (signed(a) - signed(b)) > 7:
    print("Signed borrow/underflow: YES")
else:
    print("Signed borrow/underflow: NO")