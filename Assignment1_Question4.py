'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
calculateGPA = input("What is your score? ")
if float(calculateGPA) >= 80 and float(calculateGPA) <= 100:
    print("Your GPA is 4.00")
elif float(calculateGPA) >= 75 and float(calculateGPA) <= 79:
    print
elif float(calculateGPA) >= 70 and float(calculateGPA) <= 74:
    print("Your GPA is 3.00") 
elif float(calculateGPA) >= 65 and float(calculateGPA) <= 69:
    print("Your GPA is 2.50")
elif float(calculateGPA) >= 60 and float(calculateGPA) <= 64:
    print("Your GPA is 2.00")
elif float(calculateGPA) >= 55 and float(calculateGPA) <= 59:
    print("Your GPA is 1.50")
elif float(calculateGPA) >= 50 and float(calculateGPA) <= 54:
    print("Your GPA is 1.00")
elif float(calculateGPA) < 50:
    print("You have failed the course and do not have a GPA")
    
getHonors = input("Input your GPA ")
if float(getHonors) >= 3.85 and float(getHonors) <= 4.00:
    print("You have received a Summa Cum Laude")
if float(getHonors) >= 3.70 and float(getHonors) <= 3.84:
    print("You have received a Magna Cum Laude")
if float(getHonors) >= 3.50 and float(getHonors) <= 3.69:
    print("You have received a Cum Laude")