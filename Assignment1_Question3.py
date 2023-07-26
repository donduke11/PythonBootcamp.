'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
P = 10000
n = 12
r = 8 / 100
t = input("What is the number of year? ")
A = P * (1 + (r / n)) ** n * float(t)
print("The amount after " + t, "year(s) is " + str(A))
