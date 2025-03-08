"""QUESTION 1 :   Muhammad Ammar Rao(FA24-BBD-056)
Write a Python code to accept marks of a student from 1-100 and display the grade 
according to the following formula. 
Grade F if marks are less than 50 
Grade E if marks are between 50 to 60 
Grade D if marks are between 61 to 70 
Grade C if marks are between 71 to 80 
Grade B if marks are between 81 to 90 
Grade A if marks are between 91 to 100"""



num=int(input("Enter Your Marks: "))

if num>=91 and num<=100:
    print('Grade A')
elif num>=81 and num<=90:
    print('Grade B')
elif num>=71 and num<=80:
    print('Grade C')
elif num>=61 and num<=70:
    print('Grade D')
elif num>=50 and num<=60:
    print('Grade E')
elif num<50:
    print('Grade F')  
else:
    print('Enter Correct Marks!')
