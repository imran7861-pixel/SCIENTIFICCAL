import math as m


def ar_m():
    j = True
    print(f"{'*' * 2}ARITHMETIC OPERATIONS{'*' * 2}")
    while j:
        print("select the option below:")
        print("1.continue 2.exit")
        n = int(input())
        if n == 1:
            a = eval(input("enter the expression: "))
            print(eval('a'))
        if n == 2:
            j = False


def bit_w():
    j = True
    print(f"{'*' * 2}BITWISE OPERATIONS{'*' * 2}")
    while j:
        print("select the option below:")
        print("1.continue 2.exit")
        n = int(input())
        if n == 1:
            print("enter two values for performing a bitwise operations")
            a = int(input())
            b = int(input())
            print(f"bitwise '|':{a | b}")
            print(f"bitwise '&':{a & b}")
            print(f"complement of {a} : {~a}")
            print(f"complement of {b} : {~b}")
            h = int(input("enter the no of bits you want to shift: "))
            print(f"leftshift of (<<) {a}  : {a << h}")
            print(f"rightshift of(>>){a}  : {a >> h}")
            print(f"leftshift of (<<) {b}  : {b << h}")
            print(f"rightshift of (>>){b} : {b >> h}")
        else:
            j = False


def tri_gn():
    j = True
    print(f"{'*' * 2}TRIGONOMETRIC OPERATIONS{'*' * 2}")
    while j:
        print("select the option below:")
        print("1.continue 2.exit")
        n = int(input())
        if n == 1:
            b = eval(input("enter a value: "))
            print(f"{'*' * 2} Trigonometric values {'*' * 2}")
            print(f" sin {(b)} = {eval('m.sin(m.radians(b))')}", end="")
            print(f" sinh{(b)} = {eval('m.sinh(m.radians(b))')}", end="")
            print(f" asin{(b)} = {eval('m.asinh(m.radians(b))')}", end="")
            print(f" asinh{(b)}= {eval('m.asinh(m.sinh(m.radians(b)))')}")
            print(f" cos {(b)} = {eval('m.cos(m.radians(b))')}", end=" ")
            print(f" cosh{(b)} = {eval('m.cosh(m.radians(b))')}", end=" ")
            print(f" acos{(b)} = {eval('m.acos(m.radians(b))')}", end=" ")
            print(f" acosh{(b)}= {eval('m.acosh(m.cosh(m.radians(b)))')}")
            print(f"tan {(b)} = {eval('m.tan(m.radians(b))')}", end=" ")
            print(f"tanh{(b)} = {eval('m.tanh(m.radians(b))')}", end=" ")
            print(f" atan{(b)} = {eval('m.atan(m.radians(b))')}", end=" ")
            print(f" atanh{(b)}= {eval('m.atanh(m.tanh(m.radians(b)))')}")
            print("important relations: 'sec: 1/cos' 'cot: 1/tan' 'cosec: 1/sin','tan: sin/cos'")
        if n == 2:
            j = False


def com_vec():
    j = True
    print(f"{'*' * 2}COMPLEX/VECTOR OPERATION{'*' * 2}")
    while j:
        print("1.complex numbers(add,sub,mul,div) 2.vectors(add,sub,mul) 3.exit")
        n = eval(input("enter your choice: "))
        if n == 1:
            class Complex:
                def __init__(self, r, i):
                    self.real = r
                    self.img = i

                def __add__(self, other):
                    return Complex(self.real + other.real, self.img + other.img)

                def __sub__(self, other):
                    return Complex(self.real - other.real, self.img - other.img)

                def __mul__(self, other):
                    m1 = self.real * other.real - self.img * other.img
                    m2 = self.real * other.img + self.img * other.real
                    return Complex(m1, m2)

                def __truediv__(self, other):
                    m1 = self.real * other.real + self.img * other.img
                    m2 = m.pow(other.real, 2) + m.pow(other.img, 2)
                    m3 = m1 / m2
                    m4 = self.img * other.real - self.real * other.img
                    m5 = m4 / m2
                    return Complex(m3, m5)

                # (ac-bd)+i(ad+bc) multiplication of two complex number
                def __str__(self):
                    if self.img < 0:
                        return f"{self.real}-{-self.img}i"
                    else:
                        return f"{self.real}+{self.img}i"

            print("complex numbers are in the format of 'a+bi' ")
            print("enter the  4 values for computing two complex numbers")
            b = eval(input("enter the first value: "))
            h = eval(input("enter the second value: "))
            d = eval(input("enter the third value: "))
            e = eval(input("enter the fourth value: "))
            c1 = Complex(b, h)
            c2 = Complex(d, e)
            print(f"the sum of two given complex number is : {c1 + c2}")
            print(f"the difference of two given complex number is: {c1 - c2}")
            print(f"the product of two given complex number is: {c1 * c2}")
            print(f"the division of two given complex number is: {c1 / c2}")

        if n == 2:
            class Vector:
                def __init__(self, vec):
                    self.vec = vec

                def __str__(self):
                    str1 = ""
                    index = 0
                    for i in self.vec:
                        str1 += f"{i}a{index}+"
                        index += 1
                    print("the sum of two given vectors is: ")
                    return str1[:-1]

                def __add__(self, other):
                    newlist = []
                    if len(self.vec) == len(other.vec):
                        for i in range(len(self.vec)):
                            newlist.append(self.vec[i] + other.vec[i])
                    else:
                        print("additions of vectors cannot be completed cuz lengths of the vectors are not same")
                    return Vector(newlist)

                def __sub__(self, other):
                    newlist = []
                    if len(self.vec) == len(other.vec):
                        for i in range(len(self.vec)):
                            newlist.append(self.vec[i] - other.vec[i])
                    else:
                        print("subtraction of vectors cannot be done cuz lengths of the vectors are not same")
                    return Vector(newlist)

                def __mul__(self, other):
                    sum = 0
                    if len(self.vec) == len(other.vec):
                        for i in range(len(self.vec)):
                            sum += (self.vec[i] * other.vec[i])
                    else:
                        print("multiplication of the vectors cannot be completed cuz vectors dimensions are not same")
                    print('''"multiplication of two vectors is always a scalar quantity(no direction)"''')
                    return f"the multiplication of two given vectors is: {sum}"

            print("maximum 3 values are allowed")
            print("enter the values for vector 1")
            a = eval(input())
            b = eval(input())
            c = eval(input())
            g = [a, b, c]
            print("enter the values for the second vector")
            d = eval(input())
            e = eval(input())
            f = eval(input())
            h = [d, e, f]
            c1 = Vector(g)
            c2 = Vector(h)
            print(f"the sum of two given vector is: {c1 + c2}")
            print(f"the difference of two given vector is:{c1 - c2}")
            print(c1 * c2)
        if n == 3:
            j = False


def oth_r():
    p = True
    print(f"{'*' * 2}OTHERS{'*' * 2}")
    while p:
        print("choose the options listed below")
        print("1.conversions(dec->bin/hex/oct) 2.fact/log/exp 3.d->f/f->d,sqr,cube,inv 4.exit")
        c = eval(input())
        if c == 1:
            b = eval(input("enter a number: "))
            print(f"Binary: {bin(b)}")
            print(f"hexadecimal : {hex(b)}")
            print(f"octal : {oct(b)}")
        if c == 2:
            b = eval(input("enter a number: "))
            print(f"fact = {m.factorial(b)}")
            print(f"log with base 10 : {m.log10(b)}")
            print(f"log with base 2 :{m.log2(b)}")
            g = eval(input("enter the specified base value: "))
            print(f" log with specified base: {m.log(b, g)}")
            print(f"radian : {m.radians(b)}")
            h = eval(input("enter the exponential(e^x) power value: "))
            print(f"e^{h}: {m.exp(h)}")

        if c == 3:
            b = eval(input("enter a number: "))
            print(f"fahrenheit :  {(b * 1.8) + 32}")
            print(f"celsius  : {(b - 32) * 0.555}")
            t = eval(input("enter a power value to calculate x^X: "))
            print(m.pow(b, t))
            print(f"sqrt of a number : {m.sqrt(b)}")
            print(f"inverse of a sqrt number: {m.isqrt(b)}")

        if c == 4:
            p = False


print("...welcome to the simulation of calculator...")
print("choose the options listed below:")
q = True
while q:
    print("1.ARITHMETIC CALCULATIONS\n2.BITWISE OPERATIONS\n3.TRIGNOMETRY\n4.CMPLX/VEC\n5.OTHERS\n6.EXIT")
    ch = int(input())
    if ch == 1:
        ar_m()
    elif ch == 2:
        bit_w()
    elif ch == 3:
        tri_gn()
    elif ch == 4:
        com_vec()
    elif ch == 5:
        oth_r()
    else:
        q = False
print("THANK YOU...!!!")
