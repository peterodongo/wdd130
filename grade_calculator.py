#ask for the percent of the test
percent = float(input("what percent did you get?"))

if percent >= 90:
    print("the grade is an A")
    
elif percent >= 80:
    print("the grade is B")
    
elif percent >=70:
    print("the grade is C")
    
elif percent >= 60:
    print("the grade is D")
    
elif percent <=60:
    print("the grade is F")

if percent >=70:
    print("congratulations! you have passed the test")
    
 #getting the last digit
 last_digit = percent % 10
 
#determine the sign
if last_digit >= 7:
    sign = "+"
elif last_digit <3:
    sign = "-"
    
else: print("sorry you have to redo the test")


    




