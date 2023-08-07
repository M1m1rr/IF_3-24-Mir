#calc
"""""
a = input('First digit : ')
action = input('Action (x, :, +, -) : ')
b = input('Second digit : ')

if action = "x"
c = int(a)*int(b)

if action = ':'
c = int(a)//int(b)

if action = '+'
c = int(a)+int(b)

if action = '-'
c = int(a)-int(b)

print(str(c))
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ndak bisa bagi 0."

def calculator():
    print("Pilih Operasi :")
    print("1. +")
    print("2. -")
    print("3. x")
    print("4. :")

    operasi = input("Operasi nomor : ")

    input0 = float(input("Input 1: "))
    input1 = float(input("Input 2: "))

    hasil = 0
    if operasi == '1':
        hasil = add(input0, input1)
    elif operasi == '2':
        hasil = subtract(input0, input1)
    elif operasi == '3':
        hasil = multiply(input0, input1)
    elif operasi == '4':
        hasil = divide(input0, input1)
    else:
        print("Tidak Valid")
        return

    print("Hasil: ", hasil)

if __name__ == "__main__":
    calculator()
