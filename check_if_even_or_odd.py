def check_divisibility(number):
    if (number / 2).is_integer():
        return "Even"
    else:
        return "Odd"

print(check_divisibility(7))  
print(check_divisibility(4))  

//this method checks for a number whether it is even or odd by subjecting it to a "divisibility by 2" check. so if its divisible by 2, it is even number, eif it is not then it is odd number
//.is_integer() is a function that checks if the result of the division is a whole number
//in this case, 7 will be Odd and 4 will be Even
