"""Write a Python code to accept temperature value from user (in centigrade) and display 
an appropriate message as below.   (Muhammad Ammar Rao(FA24-BBD-056))
FREEZING if temperature in less than 0 
COLD if temperature is between 0 to 15 
WARM if temperature is between 16 to 30 
HOT if temperature is between 31 to 40 
VERY HOT if temperature is greater than 40 """


user=int(input("Enter Temperature in Centigrades: "))
if user<0:
    print("FREEZING")    
elif user>0 and user<=15:
    print("COLD")
elif  user>15 and user<=30: 
    print("WARM")
elif  user>30 and user<=40:
    print("HOT")
elif user>40:
    print("VERY HOT") 
else:
    print("Enter Valid Temperature!")                 