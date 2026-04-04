def valid_4bit(bits):
    return len(bits) == 4 and all(b in "01" for b in bits)

a = input("Enter 4-bit binary number A: ")
b = input("Enter 4-bit binary number B: ")

while not valid_4bit(a):
	a = input("Invalid input. Enter exactly 4 bits for A: ")
while not valid_4bit(b):
	b = input("Invalid input. Enter exactly 4 bits for B: ")

print("A=", a)
print("B=", b)
