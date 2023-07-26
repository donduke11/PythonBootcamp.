'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def is_triangle(a, b, c):
    if a + b < c or a + c < b or c + b < a:
        return"False"
    else:
        return"True"
trial= is_triangle(1, 1, 5)
print(trial)