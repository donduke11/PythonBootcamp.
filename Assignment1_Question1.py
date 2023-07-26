'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
hwWeight = 0.4
examWeight = 0.5
discussionWeight = 0.1 
 
name = input("What is your name? ")
print("Hello " + name)
hw_grade = input("What is your homework grade? ")
exam_grade = input("What is your exam grade? ")
discussion_grade = input("What is your discussion grade? ")
total_hw = hwWeight * int(hw_grade)
total_exam = examWeight * int(exam_grade)
total_discussion = discussionWeight * int(discussion_grade)
total_grade = total_hw + total_exam + total_discussion
print(name + " your total grade is " + str(total_grade))