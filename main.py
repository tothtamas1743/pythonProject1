number = 5
number2 = number * 2
print("A number változó értéke:", number, "Ha megszorzom 2-vel, akkor ", number2, "\b-t kapok")
print("A number változó értéke:", number, "Ha megszorzom 2-vel, akkor ", number2, "-t kapok", sep="")
print(f"A number változó értéke:, {number}, Ha megszorzom 2-vel, akkor , {number2}, -t kapok",)
print("A number változó értéke: {}, Ha megszorzom 2-vel, akkor {}-t kapok" .format(number, number2))

number = 12345678987654321
print(f"A szám binális alakja: {number:b}, az oktális alakja: {number:o}, a decimális alakja: {number:d}, a hexidecimális alakja: {number:x} és {number:X} ")

