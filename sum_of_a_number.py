def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

print(sum_of_digits(1234))  

//This function basically separates all the digits that make mup the  number and calculates the sum of digits of the number, 
// eg 1234 will become 1+2+3+4 which = 10
